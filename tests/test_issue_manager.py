import json
from unittest.mock import patch, MagicMock

from src.fetcher import Paper
from src.issue_manager import (
    normalize_arxiv_id,
    is_already_posted,
    format_issue_body,
)


def test_normalize_arxiv_id_removes_version():
    assert normalize_arxiv_id("2401.12345v1") == "2401.12345"
    assert normalize_arxiv_id("2401.12345v2") == "2401.12345"
    assert normalize_arxiv_id("2401.12345v10") == "2401.12345"


def test_normalize_arxiv_id_no_version():
    assert normalize_arxiv_id("2401.12345") == "2401.12345"


def _make_paper() -> Paper:
    return Paper(
        source_id="2401.12345v1",
        title="Test Paper",
        authors=["Alice", "Bob"],
        abstract="This is a test abstract.",
        url="https://arxiv.org/abs/2401.12345v1",
        pdf_url="https://arxiv.org/pdf/2401.12345v1",
        categories=["cs.AI", "cs.SE"],
        primary_category="cs.AI",
        published="2024-01-15",
    )


@patch("src.issue_manager.subprocess.run")
def test_is_already_posted_true(mock_run):
    mock_run.return_value = MagicMock(
        returncode=0,
        stdout=json.dumps([{"title": "[2401.12345v1] Test Paper"}]),
    )
    assert is_already_posted("2401.12345v2") is True


@patch("src.issue_manager.subprocess.run")
def test_is_already_posted_false(mock_run):
    mock_run.return_value = MagicMock(
        returncode=0,
        stdout=json.dumps([]),
    )
    assert is_already_posted("2401.99999v1") is False


@patch("src.issue_manager.subprocess.run")
def test_is_already_posted_gh_failure(mock_run):
    mock_run.return_value = MagicMock(returncode=1, stdout="")
    assert is_already_posted("2401.12345v1") is False


def test_format_issue_body_contains_key_info():
    paper = _make_paper()
    body = format_issue_body(paper)
    assert "Test Paper" in body
    assert "Alice" in body
    assert "Bob" in body
    assert "2024-01-15" in body
    assert "`cs.AI`" in body
    assert "[abs]" in body
    assert "[pdf]" in body
    assert "This is a test abstract." in body
