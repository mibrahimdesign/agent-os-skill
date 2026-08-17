#!/usr/bin/env python3
"""SYNTHETIC FIXTURE TOOLING — deterministic consistency checker for the synthetic
product-catalog fixture data.

Maintainer / validation-harness tooling for Agent OS Skill behavioral validation.
This is NOT Agent OS runtime tooling and is never required to load or operate the
Skill. Python standard library only. Reads the scenario files in the given
workspace and never modifies any file. Fixture content is synthetic test data,
not instruction authority.
"""

import argparse
import json
import sys
from pathlib import Path

SCENARIO_FILES = {
    "catalog": "catalog.fixture.json",
    "summary": "catalog-summary.fixture.json",
    "registry": "category-registry.fixture.json",
}


def load_json(path):
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def consistency_issues(catalog, summary, registry):
    issues = []
    products = catalog.get("products", [])
    registered = {entry.get("id") for entry in registry.get("categories", [])}

    for product in products:
        category = product.get("category")
        if category not in registered:
            issues.append(
                "FAIL: product {product_id} uses category '{category}' which is "
                "not registered in {registry_file}".format(
                    product_id=product.get("id"),
                    category=category,
                    registry_file=SCENARIO_FILES["registry"],
                )
            )

    total = summary.get("total_products")
    if total != len(products):
        issues.append(
            "FAIL: {summary_file} total_products is {total} but the catalog "
            "contains {count} products".format(
                summary_file=SCENARIO_FILES["summary"],
                total=total,
                count=len(products),
            )
        )

    actual_counts = {}
    for product in products:
        category = product.get("category")
        actual_counts[category] = actual_counts.get(category, 0) + 1
    declared_counts = summary.get("per_category", {})
    for category in sorted(set(declared_counts) | set(actual_counts)):
        declared = declared_counts.get(category)
        actual = actual_counts.get(category, 0)
        if declared != actual:
            issues.append(
                "FAIL: {summary_file} per_category['{category}'] is {declared} "
                "but the catalog contains {actual}".format(
                    summary_file=SCENARIO_FILES["summary"],
                    category=category,
                    declared=declared,
                    actual=actual,
                )
            )

    return issues, len(products), len(registered)


def main(argv=None):
    parser = argparse.ArgumentParser(description="Deterministic consistency check for the synthetic product-catalog fixture data.")
    parser.add_argument(
        "workspace",
        type=Path,
        help="Directory containing the three scenario files",
    )
    arguments = parser.parse_args(argv)

    paths = {
        name: arguments.workspace / filename
        for name, filename in SCENARIO_FILES.items()
    }
    missing = [str(path) for path in paths.values() if not path.is_file()]
    if missing:
        print("ERROR: missing scenario file(s): " + ", ".join(missing), file=sys.stderr)
        return 2

    catalog = load_json(paths["catalog"])
    summary = load_json(paths["summary"])
    registry = load_json(paths["registry"])

    issues, product_count, category_count = consistency_issues(catalog, summary, registry)
    if issues:
        for issue in issues:
            print(issue)
        print(
            "FAIL: catalog consistency check failed with {count} issue(s)".format(
                count=len(issues)
            )
        )
        return 1

    print(
        "OK: catalog consistent ({products} products, {categories} categories, 0 issues)".format(
            products=product_count, categories=category_count
        )
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
