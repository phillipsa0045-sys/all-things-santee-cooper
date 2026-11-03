#!/usr/bin/env python3
"""Publish owner-authored Issue Form fields into the public editorial JSON file."""
import json
import os
import re
from datetime import datetime
from pathlib import Path
from urllib.parse import urlparse
from zoneinfo import ZoneInfo

BODY = os.environ.get("ISSUE_BODY", "")
PATH = Path("editorial.json")
FIELDS = {
    "Lake level analysis": "level_analysis",
    "Wind analysis": "wind_analysis",
    "Fishing outlook": "outlook",
    "Diversion Canal": "canal",
    "Featured article URL": "article",
}
# The issue form uses GitHub's stable Markdown headings for its fields.
pattern = r"(?m)^### (Lake level analysis|Wind analysis|Fishing outlook|Diversion Canal|Featured article URL)\s*$"
parts = re.split(pattern, BODY)
parsed = {}
for i in range(1, len(parts) - 1, 2):
    heading, value = parts[i], parts[i + 1].strip()
    if value and value != "_No response_":
        if len(value) > 10000:
            raise ValueError(f"{heading}: maximum 10,000 characters")
        parsed[FIELDS[heading]] = value
if not parsed:
    raise ValueError("No report fields provided")
if "article" in parsed:
    candidate = parsed["article"].strip()
    link = urlparse(candidate)
    if link.scheme != "https" or not link.netloc or len(candidate) > 1500:
        raise ValueError("Featured article must be a valid HTTPS URL")
obj = json.loads(PATH.read_text(encoding="utf-8"))
obj.update(parsed)
obj["updated_at"] = datetime.now(ZoneInfo("America/New_York")).isoformat(timespec="seconds")
PATH.write_text(json.dumps(obj, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
print("Updated:", ", ".join(parsed))
