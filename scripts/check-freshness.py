#!/usr/bin/env python3
"""Check field freshness and report stale content."""

import sys
from datetime import datetime, timedelta
from pathlib import Path

import yaml

STALE_THRESHOLD_DAYS = 180  # 6 months
WARNING_THRESHOLD_DAYS = 90  # 3 months


def extract_frontmatter(file_path: Path) -> dict | None:
    content = file_path.read_text()
    if not content.startswith("---"):
        return None
    parts = content.split("---", 2)
    if len(parts) < 3:
        return None
    try:
        return yaml.safe_load(parts[1])
    except yaml.YAMLError:
        return None


def check_date(date_str: str, threshold_days: int) -> tuple[bool, int]:
    try:
        date = datetime.strptime(str(date_str), "%Y-%m-%d")
        age_days = (datetime.now() - date).days
        return age_days > threshold_days, age_days
    except (ValueError, TypeError):
        return True, -1


def main():
    fields_dir = Path("fields")
    today = datetime.now().strftime("%Y-%m-%d")
    stale_fields = []
    stale_tools = []
    missing_content = []

    print(f"## Freshness Report — {today}\n")

    for field_dir in sorted(fields_dir.iterdir()):
        if not field_dir.is_dir() or field_dir.name.startswith("_"):
            continue

        overview = field_dir / "overview.md"
        if not overview.exists():
            missing_content.append((field_dir.name, "overview.md missing"))
            continue

        fm = extract_frontmatter(overview)
        if not fm:
            missing_content.append((field_dir.name, "invalid frontmatter"))
            continue

        # Check overview freshness
        is_stale, age = check_date(fm.get("last_verified", ""), STALE_THRESHOLD_DAYS)
        if is_stale:
            stale_fields.append((field_dir.name, fm.get("last_verified", "unknown"), age))

        # Check tools freshness
        tools_file = field_dir / "tools.yml"
        if tools_file.exists():
            with open(tools_file) as f:
                try:
                    tools = yaml.safe_load(f) or []
                except yaml.YAMLError:
                    tools = []

            for tool in tools:
                if isinstance(tool, dict):
                    is_tool_stale, tool_age = check_date(
                        tool.get("last_verified", ""), STALE_THRESHOLD_DAYS
                    )
                    if is_tool_stale:
                        stale_tools.append((field_dir.name, tool.get("name", "unknown"), tool_age))

        # Check for empty/missing files
        for required in ["tools.yml", "automation.md", "skills.md", "career.md"]:
            req_path = field_dir / required
            if not req_path.exists():
                missing_content.append((field_dir.name, f"{required} missing"))
            elif req_path.stat().st_size < 100:
                missing_content.append((field_dir.name, f"{required} appears empty"))

    # Report
    if stale_fields:
        print("### Stale Fields (not verified in 6+ months)\n")
        print("| Field | Last Verified | Days Stale |")
        print("|-------|--------------|------------|")
        for name, last_verified, age in stale_fields:
            print(f"| {name} | {last_verified} | {age} |")
        print()

    if stale_tools:
        print("### Stale Tools\n")
        print("| Field | Tool | Days Stale |")
        print("|-------|------|------------|")
        for field, tool, age in stale_tools:
            print(f"| {field} | {tool} | {age} |")
        print()

    if missing_content:
        print("### Missing Content\n")
        print("| Field | Issue |")
        print("|-------|-------|")
        for field, issue in missing_content:
            print(f"| {field} | {issue} |")
        print()

    if not stale_fields and not stale_tools and not missing_content:
        print("All fields are fresh and complete!")

    total_issues = len(stale_fields) + len(stale_tools) + len(missing_content)
    if total_issues > 0:
        sys.exit(0)  # Don't fail CI, just report


if __name__ == "__main__":
    main()
