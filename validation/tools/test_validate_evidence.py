#!/usr/bin/env python3
"""Dependency-free contract tests for the evidence validator."""

import copy
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


REPOSITORY_ROOT = Path(__file__).resolve().parents[2]
VALIDATOR = REPOSITORY_ROOT / "validation/tools/validate_evidence.py"
SCHEMA = REPOSITORY_ROOT / "validation/schemas/evidence-result.schema.json"
FIXTURES = REPOSITORY_ROOT / "validation/tools/fixtures"

EXPECTED_REQUIRED_FIELDS = {
    "run_id",
    "attempt",
    "test_id",
    "skill_version",
    "runtime_baseline",
    "fixture_version",
    "rubric_version",
    "transcript_ref",
    "model",
    "host",
    "mode",
    "result",
    "evidence_level",
    "evaluator",
    "date",
    "deviation",
    "sanitized",
    "checks",
    "observed_capability_profile",
    "notes",
}


def read_json(name):
    with (FIXTURES / name).open(encoding="utf-8") as handle:
        return json.load(handle)


class ValidatorHarness:
    def __init__(self, record, transcript=True, schema_path=SCHEMA):
        self.record = copy.deepcopy(record)
        self.transcript = transcript
        self.schema_path = Path(schema_path)
        self._temporary = None
        self.root = None
        self.result_path = None

    def __enter__(self):
        self._temporary = tempfile.TemporaryDirectory(prefix="agent-os-evidence-")
        self.root = Path(self._temporary.name)
        run_id = self.record.get("run_id", "20260817-aos-t001-reference-model-reference-host")
        attempt = self.record.get("attempt", 1)
        result_directory = self.root / "validation/results" / run_id
        result_directory.mkdir(parents=True)
        self.result_path = result_directory / f"attempt-{attempt:02d}.json"
        self.result_path.write_text(json.dumps(self.record, indent=2) + "\n", encoding="utf-8")

        transcript_ref = self.record.get("transcript_ref")
        if self.transcript and transcript_ref:
            transcript_path = self.root / transcript_ref
            transcript_path.parent.mkdir(parents=True)
            transcript_path.write_text(
                (FIXTURES / "sanitized-transcript.fixture.md").read_text(encoding="utf-8"),
                encoding="utf-8",
            )
        return self

    def run(self, *extra_arguments):
        return subprocess.run(
            [
                sys.executable,
                str(VALIDATOR),
                str(self.result_path),
                "--repo-root",
                str(self.root),
                "--schema",
                str(self.schema_path),
                *extra_arguments,
            ],
            cwd=REPOSITORY_ROOT,
            capture_output=True,
            text=True,
            check=False,
        )

    def __exit__(self, exc_type, exc_value, traceback):
        temporary_path = self.root
        self._temporary.cleanup()
        if temporary_path.exists():
            raise AssertionError(f"temporary evidence root was not removed: {temporary_path}")


class EvidenceValidatorTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.live = read_json("valid-live-observed.json")
        cls.not_executed = read_json("valid-not-executed.json")
        if SCHEMA.exists():
            with SCHEMA.open(encoding="utf-8") as handle:
                cls.schema = json.load(handle)
        else:
            cls.schema = {"required": []}

    def assert_valid(self, record, transcript=True):
        with ValidatorHarness(record, transcript=transcript) as harness:
            completed = harness.run()
        self.assertEqual(completed.returncode, 0, completed.stdout + completed.stderr)

    def assert_invalid(self, record, expected_code, transcript=True):
        with ValidatorHarness(record, transcript=transcript) as harness:
            completed = harness.run()
        self.assertEqual(completed.returncode, 1, completed.stdout + completed.stderr)
        self.assertIn(expected_code, completed.stdout + completed.stderr)

    def test_valid_live_observed_reference_passes(self):
        self.assert_valid(self.live)

    def test_valid_not_executed_reference_passes(self):
        self.assert_valid(self.not_executed, transcript=False)

    def test_schema_contract_inventory_matches_required_fields_and_enums(self):
        self.assertEqual(set(self.schema["required"]), EXPECTED_REQUIRED_FIELDS)
        properties = self.schema["properties"]
        definitions = self.schema["$defs"]
        self.assertEqual(properties["mode"]["enum"], ["FULL", "LIMITED", "EMBEDDED"])
        self.assertEqual(
            properties["result"]["enum"],
            ["PASS", "PARTIAL", "FAIL", "BLOCKED", "NOT_EXECUTED"],
        )
        self.assertEqual(
            properties["evidence_level"]["anyOf"][0]["enum"],
            ["STATIC_REVIEW", "SELF_SIMULATED", "LIVE_OBSERVED", "LIVE_INDEPENDENT"],
        )
        self.assertEqual(
            definitions["evaluator"]["properties"]["type"]["enum"],
            ["SAME_OPERATOR", "OTHER_OPERATOR", "EXTERNAL_VALIDATOR"],
        )
        self.assertEqual(definitions["check"]["properties"]["kind"]["enum"], ["machine", "human"])
        self.assertEqual(
            definitions["check"]["properties"]["result"]["enum"],
            ["PASS", "FAIL", "NOT_APPLICABLE"],
        )
        self.assertEqual(definitions["nullableVersion"]["anyOf"][0], {"type": "null"})

    def test_all_schema_required_fields_are_enforced(self):
        for field in self.schema["required"]:
            with self.subTest(field=field):
                record = copy.deepcopy(self.live)
                del record[field]
                self.assert_invalid(record, "SCHEMA_VALIDATION")

    def test_nested_schema_required_fields_are_enforced(self):
        paths = (
            ("model", "version"),
            ("host", "id"),
            ("evaluator", "independent"),
            ("deviation", "description"),
            ("observed_capability_profile", "filesystem_read"),
        )
        for parent, field in paths:
            with self.subTest(parent=parent, field=field):
                record = copy.deepcopy(self.live)
                del record[parent][field]
                self.assert_invalid(record, "SCHEMA_VALIDATION")

    def test_schema_enums_are_enforced(self):
        mutations = (
            (("mode",), "INVALID_MODE"),
            (("result",), "INVALID_RESULT"),
            (("evidence_level",), "INVALID_EVIDENCE"),
            (("model", "class"), "INVALID_MODEL_CLASS"),
            (("host", "class"), "INVALID_HOST_CLASS"),
            (("evaluator", "type"), "INVALID_EVALUATOR"),
            (("checks", 0, "kind"), "INVALID_KIND"),
            (("checks", 0, "result"), "INVALID_CHECK_RESULT"),
        )
        for path_parts, value in mutations:
            with self.subTest(path=path_parts):
                record = copy.deepcopy(self.live)
                target = record
                for part in path_parts[:-1]:
                    target = target[part]
                target[path_parts[-1]] = value
                self.assert_invalid(record, "SCHEMA_VALIDATION")

    def test_null_versions_are_honest_and_valid(self):
        record = copy.deepcopy(self.live)
        record["model"]["version"] = None
        record["host"]["version"] = None
        self.assert_valid(record)

    def test_placeholder_versions_are_rejected(self):
        for field, value in (("model", "unknown"), ("host", "N/A")):
            with self.subTest(field=field, value=value):
                record = copy.deepcopy(self.live)
                record[field]["version"] = value
                self.assert_invalid(record, "SCHEMA_VALIDATION")

    def test_result_and_evidence_level_compatibility(self):
        record = copy.deepcopy(self.live)
        record["evidence_level"] = None
        self.assert_invalid(record, "SCHEMA_VALIDATION")

        record = copy.deepcopy(self.not_executed)
        record["evidence_level"] = "STATIC_REVIEW"
        self.assert_invalid(record, "SCHEMA_VALIDATION", transcript=False)

    def test_same_operator_cannot_be_independent(self):
        record = copy.deepcopy(self.live)
        record["evaluator"]["independent"] = True
        self.assert_invalid(record, "SCHEMA_VALIDATION")

    def test_live_observed_requires_transcript_reference(self):
        record = copy.deepcopy(self.live)
        record["transcript_ref"] = None
        self.assert_invalid(record, "SCHEMA_VALIDATION", transcript=False)

    def test_live_observed_requires_sanitized_true(self):
        record = copy.deepcopy(self.live)
        record["sanitized"] = False
        self.assert_invalid(record, "SCHEMA_VALIDATION")

    def test_live_independent_requires_independent_non_same_operator(self):
        record = copy.deepcopy(self.live)
        record["evidence_level"] = "LIVE_INDEPENDENT"
        record["evaluator"] = {"type": "SAME_OPERATOR", "independent": False}
        self.assert_invalid(record, "SCHEMA_VALIDATION")

    def test_live_independent_requires_sanitized_true(self):
        record = copy.deepcopy(self.live)
        record["evidence_level"] = "LIVE_INDEPENDENT"
        record["evaluator"] = {"type": "EXTERNAL_VALIDATOR", "independent": True}
        record["sanitized"] = False
        self.assert_invalid(record, "SCHEMA_VALIDATION")

    def test_live_independent_requires_exact_model_and_host_ids(self):
        for field in ("model", "host"):
            with self.subTest(field=field):
                record = copy.deepcopy(self.live)
                record["evidence_level"] = "LIVE_INDEPENDENT"
                record["evaluator"] = {"type": "EXTERNAL_VALIDATOR", "independent": True}
                record[field]["id"] = None
                self.assert_invalid(record, "SCHEMA_VALIDATION")

    def test_valid_live_independent_accepts_null_versions(self):
        record = copy.deepcopy(self.live)
        record["evidence_level"] = "LIVE_INDEPENDENT"
        record["evaluator"] = {"type": "EXTERNAL_VALIDATOR", "independent": True}
        record["model"]["version"] = None
        record["host"]["version"] = None
        self.assert_valid(record)

    def test_not_executed_requires_null_evidence(self):
        record = copy.deepcopy(self.not_executed)
        record["evidence_level"] = "SELF_SIMULATED"
        self.assert_invalid(record, "SCHEMA_VALIDATION", transcript=False)

    def test_transcript_must_exist(self):
        self.assert_invalid(self.live, "TRANSCRIPT_NOT_FOUND", transcript=False)

    def test_transcript_reference_cannot_traverse(self):
        record = copy.deepcopy(self.live)
        record["transcript_ref"] = "../private.md"
        self.assert_invalid(record, "SCHEMA_VALIDATION", transcript=False)

    def test_transcript_reference_must_match_run_and_attempt(self):
        record = copy.deepcopy(self.live)
        record["transcript_ref"] = (
            "validation/transcripts/20260817-aos-t001-other-model-other-host/attempt-01.md"
        )
        self.assert_invalid(record, "TRANSCRIPT_PATH_MISMATCH", transcript=False)

    def test_run_id_must_match_exact_model_and_host_ids(self):
        record = copy.deepcopy(self.live)
        record["model"]["id"] = "different-model"
        self.assert_invalid(record, "RUN_ID_MISMATCH")

    def test_run_date_must_match_run_id(self):
        record = copy.deepcopy(self.live)
        record["date"] = "2026-08-18"
        self.assert_invalid(record, "RUN_DATE_MISMATCH")

    def test_attempt_path_must_match_attempt(self):
        with ValidatorHarness(self.live) as harness:
            mismatched = harness.result_path.with_name("attempt-02.json")
            harness.result_path.rename(mismatched)
            harness.result_path = mismatched
            completed = harness.run()
        self.assertEqual(completed.returncode, 1, completed.stdout + completed.stderr)
        self.assertIn("RESULT_PATH_MISMATCH", completed.stdout + completed.stderr)

    def test_duplicate_json_keys_fail(self):
        with ValidatorHarness(self.live) as harness:
            harness.result_path.write_text('{"run_id":"first","run_id":"second"}\n', encoding="utf-8")
            completed = harness.run()
        self.assertEqual(completed.returncode, 1, completed.stdout + completed.stderr)
        self.assertIn("DUPLICATE_JSON_KEY", completed.stdout + completed.stderr)

    def test_schema_validator_parity_matrix(self):
        cases = [
            ("LIVE_OBSERVED", {"type": "SAME_OPERATOR", "independent": False}, True, "path"),
            ("LIVE_INDEPENDENT", {"type": "EXTERNAL_VALIDATOR", "independent": True}, True, "path"),
            (None, {"type": "SAME_OPERATOR", "independent": False}, True, None),
        ]
        for evidence_level, evaluator, sanitized, transcript_marker in cases:
            with self.subTest(evidence_level=evidence_level):
                record = copy.deepcopy(self.live if evidence_level else self.not_executed)
                record["evidence_level"] = evidence_level
                record["evaluator"] = evaluator
                record["sanitized"] = sanitized
                if transcript_marker is None:
                    record["transcript_ref"] = None
                self.assert_valid(record, transcript=transcript_marker is not None)

    def test_unsupported_schema_keyword_fails_closed(self):
        with tempfile.TemporaryDirectory(prefix="agent-os-schema-") as temporary:
            schema_path = Path(temporary) / "schema.json"
            schema = copy.deepcopy(self.schema)
            schema["unsupportedValidationKeyword"] = True
            schema_path.write_text(json.dumps(schema), encoding="utf-8")
            with ValidatorHarness(self.live, schema_path=schema_path) as harness:
                completed = harness.run()
        self.assertEqual(completed.returncode, 2, completed.stdout + completed.stderr)
        self.assertIn("UNSUPPORTED_SCHEMA_KEYWORD", completed.stdout + completed.stderr)

    def test_temporary_artifacts_and_worktree_are_unchanged(self):
        before = subprocess.run(
            ["git", "status", "--porcelain=v1"],
            cwd=REPOSITORY_ROOT,
            capture_output=True,
            text=True,
            check=True,
        ).stdout
        with ValidatorHarness(self.live) as harness:
            temporary_root = harness.root
            completed = harness.run()
            self.assertEqual(completed.returncode, 0, completed.stdout + completed.stderr)
        self.assertFalse(temporary_root.exists())
        after = subprocess.run(
            ["git", "status", "--porcelain=v1"],
            cwd=REPOSITORY_ROOT,
            capture_output=True,
            text=True,
            check=True,
        ).stdout
        self.assertEqual(before, after)


if __name__ == "__main__":
    unittest.main(verbosity=2)
