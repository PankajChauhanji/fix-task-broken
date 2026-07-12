import json
from pathlib import Path


def test_report_exists():
    """The agent produced a report file."""
    assert Path("/app/report.json").exists(), "no report.json found"


def test_report_content():
    """The report file contains the correct summary stats."""
    content = Path("/app/report.json").read_text()
    data = json.loads(content)
    
    assert data.get("total_requests") == 6, "total_requests should be 6"
    assert data.get("unique_ips") == 3, "unique_ips should be 3"
    assert data.get("top_path") == "/index.html", "top_path should be /index.html"
