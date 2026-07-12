import json
import pytest
from pathlib import Path

@pytest.fixture
def report_data():
    assert Path("/app/report.json").exists(), "no /app/report.json found"
    return json.loads(Path("/app/report.json").read_text())

def test_criterion_1(report_data):
    """1. The JSON object contains a `total_requests` key with the total number of requests in the log file."""
    assert report_data.get("total_requests") == 6, "total_requests should be 6"

def test_criterion_2(report_data):
    """2. The JSON object contains a `unique_ips` key with the total number of unique client IP addresses involved."""
    assert report_data.get("unique_ips") == 3, "unique_ips should be 3"

def test_criterion_3(report_data):
    """3. The JSON object contains a `top_path` key with the single most frequently requested path."""
    assert report_data.get("top_path") == "/index.html", "top_path should be /index.html"
