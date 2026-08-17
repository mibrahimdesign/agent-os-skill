#!/usr/bin/env python3
"""Validate Agent OS evidence records using the normative JSON Schema.

This is optional MAINTAINER_VALIDATION_TOOLING. Agent OS Skill does not need
Python or this script at runtime.
"""

import argparse
import json
import re
import sys
from datetime import date
from pathlib import Path


SCHEMA_VALIDATION = "SCHEMA_VALIDATION"
PROJECT_VALIDATION_RULE = "PROJECT_VALIDATION_RULE"

ANNOTATION_KEYWORDS = {"$schema", "$id", "title", "description", "default", "examples"}
VALIDATION_KEYWORDS = {
    "$ref",
    "$defs",
    "type",
    "required",
    "properties",
    "additionalProperties",
    "enum",
    "const",
    "pattern",
    "format",
    "minLength",
    "maxLength",
    "minimum",
    "items",
    "minItems",
    "maxItems",
    "uniqueItems",
    "allOf",
    "anyOf",
    "oneOf",
    "not",
    "if",
    "then",
    "else",
}


class DuplicateKeyError(ValueError):
    pass


class UnsupportedSchemaKeyword(ValueError):
    pass


def reject_duplicate_keys(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise DuplicateKeyError(key)
        result[key] = value
    return result


def load_json(path):
    with path.open(encoding="utf-8") as handle:
        return json.load(handle, object_pairs_hook=reject_duplicate_keys)


def assert_supported_schema(schema, location="#"):
    if not isinstance(schema, dict):
        raise UnsupportedSchemaKeyword(f"{location}: schema node must be an object")

    for keyword, value in schema.items():
        if keyword not in ANNOTATION_KEYWORDS and keyword not in VALIDATION_KEYWORDS:
            raise UnsupportedSchemaKeyword(f"{location}: unsupported keyword {keyword!r}")

        if keyword in {"properties", "$defs"}:
            if not isinstance(value, dict):
                raise UnsupportedSchemaKeyword(f"{location}/{keyword}: expected an object")
            for name, child in value.items():
                assert_supported_schema(child, f"{location}/{keyword}/{name}")
        elif keyword in {"items", "not", "if", "then", "else", "additionalProperties"}:
            if isinstance(value, dict):
                assert_supported_schema(value, f"{location}/{keyword}")
            elif keyword == "additionalProperties" and isinstance(value, bool):
                continue
            else:
                raise UnsupportedSchemaKeyword(f"{location}/{keyword}: unsupported value")
        elif keyword in {"allOf", "anyOf", "oneOf"}:
            if not isinstance(value, list):
                raise UnsupportedSchemaKeyword(f"{location}/{keyword}: expected an array")
            for index, child in enumerate(value):
                assert_supported_schema(child, f"{location}/{keyword}/{index}")


def resolve_reference(root_schema, reference):
    if not reference.startswith("#/"):
        raise UnsupportedSchemaKeyword(f"external schema reference is unsupported: {reference}")
    value = root_schema
    for part in reference[2:].split("/"):
        key = part.replace("~1", "/").replace("~0", "~")
        if not isinstance(value, dict) or key not in value:
            raise UnsupportedSchemaKeyword(f"unresolved schema reference: {reference}")
        value = value[key]
    if not isinstance(value, dict):
        raise UnsupportedSchemaKeyword(f"schema reference is not an object: {reference}")
    return value


def instance_has_type(instance, expected):
    if expected == "null":
        return instance is None
    if expected == "boolean":
        return isinstance(instance, bool)
    if expected == "integer":
        return isinstance(instance, int) and not isinstance(instance, bool)
    if expected == "number":
        return isinstance(instance, (int, float)) and not isinstance(instance, bool)
    if expected == "string":
        return isinstance(instance, str)
    if expected == "array":
        return isinstance(instance, list)
    if expected == "object":
        return isinstance(instance, dict)
    raise UnsupportedSchemaKeyword(f"unsupported JSON Schema type: {expected}")


def schema_errors(instance, schema, root_schema, location="$"):
    errors = []

    if "$ref" in schema:
        errors.extend(schema_errors(instance, resolve_reference(root_schema, schema["$ref"]), root_schema, location))

    if "allOf" in schema:
        for child in schema["allOf"]:
            errors.extend(schema_errors(instance, child, root_schema, location))

    if "anyOf" in schema:
        alternatives = [schema_errors(instance, child, root_schema, location) for child in schema["anyOf"]]
        if not any(not alternative for alternative in alternatives):
            errors.append(f"{location}: does not match any allowed schema")

    if "oneOf" in schema:
        matches = sum(not schema_errors(instance, child, root_schema, location) for child in schema["oneOf"])
        if matches != 1:
            errors.append(f"{location}: must match exactly one allowed schema")

    if "not" in schema and not schema_errors(instance, schema["not"], root_schema, location):
        errors.append(f"{location}: matches a prohibited schema")

    if "if" in schema:
        condition_matches = not schema_errors(instance, schema["if"], root_schema, location)
        selected = schema.get("then") if condition_matches else schema.get("else")
        if selected is not None:
            errors.extend(schema_errors(instance, selected, root_schema, location))

    if "const" in schema and instance != schema["const"]:
        errors.append(f"{location}: must equal {schema['const']!r}")

    if "enum" in schema and instance not in schema["enum"]:
        errors.append(f"{location}: value {instance!r} is not in the allowed enum")

    if "type" in schema:
        expected_types = schema["type"] if isinstance(schema["type"], list) else [schema["type"]]
        if not any(instance_has_type(instance, expected) for expected in expected_types):
            errors.append(f"{location}: expected type {' | '.join(expected_types)}")
            return errors

    if isinstance(instance, dict):
        for required in schema.get("required", []):
            if required not in instance:
                errors.append(f"{location}: missing required property {required!r}")

        properties = schema.get("properties", {})
        for name, child in properties.items():
            if name in instance:
                errors.extend(schema_errors(instance[name], child, root_schema, f"{location}.{name}"))

        if schema.get("additionalProperties") is False:
            for name in instance:
                if name not in properties:
                    errors.append(f"{location}: unknown property {name!r}")

    if isinstance(instance, list):
        if "minItems" in schema and len(instance) < schema["minItems"]:
            errors.append(f"{location}: requires at least {schema['minItems']} items")
        if "maxItems" in schema and len(instance) > schema["maxItems"]:
            errors.append(f"{location}: permits at most {schema['maxItems']} items")
        if schema.get("uniqueItems"):
            serialized = [json.dumps(item, sort_keys=True) for item in instance]
            if len(serialized) != len(set(serialized)):
                errors.append(f"{location}: array items must be unique")
        if "items" in schema:
            for index, item in enumerate(instance):
                errors.extend(schema_errors(item, schema["items"], root_schema, f"{location}[{index}]"))

    if isinstance(instance, str):
        if "minLength" in schema and len(instance) < schema["minLength"]:
            errors.append(f"{location}: string is shorter than {schema['minLength']}")
        if "maxLength" in schema and len(instance) > schema["maxLength"]:
            errors.append(f"{location}: string is longer than {schema['maxLength']}")
        if "pattern" in schema and re.search(schema["pattern"], instance) is None:
            errors.append(f"{location}: does not match required pattern")
        if schema.get("format") == "date":
            try:
                parsed = date.fromisoformat(instance)
                if parsed.isoformat() != instance:
                    raise ValueError
            except ValueError:
                errors.append(f"{location}: expected an ISO YYYY-MM-DD date")
        elif "format" in schema:
            raise UnsupportedSchemaKeyword(f"unsupported JSON Schema format: {schema['format']}")

    if isinstance(instance, (int, float)) and not isinstance(instance, bool):
        if "minimum" in schema and instance < schema["minimum"]:
            errors.append(f"{location}: value is below minimum {schema['minimum']}")

    return errors


def slug(value):
    normalized = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")
    return normalized


def safe_relative_path(repository_root, reference):
    if not isinstance(reference, str):
        return None
    candidate = (repository_root / reference).resolve()
    try:
        candidate.relative_to(repository_root.resolve())
    except ValueError:
        return None
    return candidate


def project_validation_errors(record, result_path, repository_root):
    errors = []
    run_id = record["run_id"]
    attempt = record["attempt"]

    expected_result = (
        repository_root / "validation/results" / run_id / f"attempt-{attempt:02d}.json"
    ).resolve()
    if result_path.resolve() != expected_result:
        errors.append(("RESULT_PATH_MISMATCH", f"expected canonical result path {expected_result}"))

    compact_date = record["date"].replace("-", "")
    if not run_id.startswith(f"{compact_date}-"):
        errors.append(("RUN_DATE_MISMATCH", "run_id date prefix does not match date"))

    model_id = record["model"]["id"]
    host_id = record["host"]["id"]
    if model_id is not None and host_id is not None:
        expected_run_id = "-".join(
            (compact_date, record["test_id"].lower(), slug(model_id), slug(host_id))
        )
        if run_id != expected_run_id:
            errors.append(("RUN_ID_MISMATCH", f"expected run_id {expected_run_id!r}"))

    transcript_ref = record["transcript_ref"]
    if transcript_ref is not None:
        expected_ref = f"validation/transcripts/{run_id}/attempt-{attempt:02d}.md"
        if transcript_ref != expected_ref:
            errors.append(("TRANSCRIPT_PATH_MISMATCH", f"expected transcript_ref {expected_ref!r}"))
        transcript_path = safe_relative_path(repository_root, transcript_ref)
        if transcript_path is None:
            errors.append(("UNSAFE_TRANSCRIPT_PATH", "transcript_ref escapes the repository root"))
        elif not transcript_path.is_file():
            errors.append(("TRANSCRIPT_NOT_FOUND", f"referenced transcript does not exist: {transcript_ref}"))

    return errors


def discover_result_files(target):
    if target.is_file():
        return [target]
    if target.is_dir():
        return sorted(target.rglob("*.json"))
    raise FileNotFoundError(target)


def validate_file(result_path, schema, repository_root):
    try:
        record = load_json(result_path)
    except DuplicateKeyError as error:
        return [("DUPLICATE_JSON_KEY", f"duplicate JSON key: {error}")]
    except (OSError, json.JSONDecodeError) as error:
        return [("INVALID_JSON", str(error))]

    structural = schema_errors(record, schema, schema)
    if structural:
        return [(SCHEMA_VALIDATION, message) for message in structural]

    return project_validation_errors(record, result_path, repository_root)


def build_parser():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("target", type=Path, help="Canonical evidence result JSON file or directory")
    parser.add_argument("--repo-root", type=Path, default=Path.cwd(), help="Repository root")
    parser.add_argument(
        "--schema",
        type=Path,
        default=None,
        help="Normative evidence schema (defaults under --repo-root)",
    )
    return parser


def main(argv=None):
    arguments = build_parser().parse_args(argv)
    repository_root = arguments.repo_root.resolve()
    schema_path = arguments.schema or repository_root / "validation/schemas/evidence-result.schema.json"

    try:
        schema = load_json(schema_path)
        assert_supported_schema(schema)
        result_files = discover_result_files(arguments.target)
    except DuplicateKeyError as error:
        print(f"[DUPLICATE_JSON_KEY] duplicate JSON key in schema: {error}", file=sys.stderr)
        return 2
    except UnsupportedSchemaKeyword as error:
        print(f"[UNSUPPORTED_SCHEMA_KEYWORD] {error}", file=sys.stderr)
        return 2
    except (OSError, json.JSONDecodeError, FileNotFoundError) as error:
        print(f"[VALIDATOR_ERROR] {error}", file=sys.stderr)
        return 2

    invalid_count = 0
    for result_file in result_files:
        errors = validate_file(result_file, schema, repository_root)
        if errors:
            invalid_count += 1
            print(f"INVALID {result_file}")
            for code, message in errors:
                classification = PROJECT_VALIDATION_RULE if code != SCHEMA_VALIDATION else SCHEMA_VALIDATION
                print(f"  [{code}] [{classification}] {message}")
        else:
            print(f"VALID {result_file}")

    print(f"Validated {len(result_files)} file(s); invalid: {invalid_count}")
    return 1 if invalid_count else 0


if __name__ == "__main__":
    sys.exit(main())
