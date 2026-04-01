#!/usr/bin/env python3
"""Validate all tools.yml files against the required schema."""

import sys
from pathlib import Path

import yaml

REQUIRED_FIELDS = {"name", "url", "category", "what_it_does", "adoption", "pricing", "added", "last_verified"}
VALID_ADOPTION = {"experimental", "emerging", "growing", "widespread"}
VALID_PRICING = {"free", "freemium", "paid", "enterprise"}

def validate_tool(tool: dict, file_path: str, index: int) -> list[str]:
    errors = []
    prefix = f"{file_path} tool #{index + 1}"

    if not isinstance(tool, dict):
        return [f"{prefix}: entry is not a dictionary"]

    tool_name = tool.get("name", f"unnamed #{index + 1}")
    prefix = f"{file_path} [{tool_name}]"

    missing = REQUIRED_FIELDS - set(tool.keys())
    if missing:
        errors.append(f"{prefix}: missing required fields: {', '.join(sorted(missing))}")

    if tool.get("adoption") and tool["adoption"] not in VALID_ADOPTION:
        errors.append(f"{prefix}: invalid adoption '{tool['adoption']}', must be one of {VALID_ADOPTION}")

    if tool.get("pricing") and tool["pricing"] not in VALID_PRICING:
        errors.append(f"{prefix}: invalid pricing '{tool['pricing']}', must be one of {VALID_PRICING}")

    if tool.get("url") and not tool["url"].startswith("http"):
        errors.append(f"{prefix}: url must start with http:// or https://")

    return errors


def main():
    fields_dir = Path("fields")
    all_errors = []

    for tools_file in sorted(fields_dir.glob("*/tools.yml")):
        if "_template" in str(tools_file):
            continue

        with open(tools_file) as f:
            try:
                tools = yaml.safe_load(f)
            except yaml.YAMLError as e:
                all_errors.append(f"{tools_file}: invalid YAML: {e}")
                continue

        if not tools or not isinstance(tools, list):
            continue

        for i, tool in enumerate(tools):
            all_errors.extend(validate_tool(tool, str(tools_file), i))

    if all_errors:
        print("Tool validation errors:")
        for error in all_errors:
            print(f"  - {error}")
        sys.exit(1)
    else:
        print("All tools.yml files are valid.")


if __name__ == "__main__":
    main()
