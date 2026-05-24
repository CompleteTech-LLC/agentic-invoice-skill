#!/usr/bin/env python3
"""List and render agentic development invoice templates."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CATALOG_MD = ROOT / "references" / "invoice-catalog.md"
INDEX_JSON = ROOT / "references" / "template-index.json"


def load_index() -> list[dict[str, str]]:
    data = json.loads(INDEX_JSON.read_text(encoding="utf-8"))
    return data["templates"]


def extract_template(template_id: str) -> str:
    text = CATALOG_MD.read_text(encoding="utf-8")
    pattern = re.compile(
        rf"^### {re.escape(template_id)}\n(?P<body>.*?)(?=^### |\Z)",
        re.MULTILINE | re.DOTALL,
    )
    match = pattern.search(text)
    if not match:
        raise KeyError(f"Template not found in invoice-catalog.md: {template_id}")
    return match.group("body").strip()


class SafeDict(dict[str, str]):
    def __missing__(self, key: str) -> str:
        return "{" + key + "}"


def parse_vars(raw_vars: list[str]) -> dict[str, str]:
    values: dict[str, str] = {}
    for raw in raw_vars:
        if "=" not in raw:
            raise ValueError(f"--var must be key=value, got: {raw}")
        key, value = raw.split("=", 1)
        key = key.strip()
        if not key:
            raise ValueError(f"--var key cannot be empty: {raw}")
        values[key] = value
    return values


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--list", action="store_true", help="List available invoice template IDs.")
    parser.add_argument("--stage", help="Filter --list by stage.")
    parser.add_argument("--type", dest="invoice_type", help="Filter --list by invoice type.")
    parser.add_argument("--template", help="Template ID to render.")
    parser.add_argument("--var", action="append", default=[], help="Placeholder value as key=value.")
    args = parser.parse_args()

    templates = load_index()
    if args.list:
        for item in templates:
            if args.stage and item["stage"] != args.stage:
                continue
            if args.invoice_type and item["type"] != args.invoice_type:
                continue
            print(f"{item['id']}\t{item['stage']}\t{item['type']}")
        return 0

    if not args.template:
        parser.error("provide --list or --template")

    ids = {item["id"] for item in templates}
    if args.template not in ids:
        print(f"Unknown template: {args.template}", file=sys.stderr)
        return 2

    values = parse_vars(args.var)
    print(extract_template(args.template).format_map(SafeDict(values)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
