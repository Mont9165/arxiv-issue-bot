from datetime import date
from pathlib import Path

from src.fetcher import Paper
from src.report import format_daily_report, get_report_path, write_daily_report


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


def test_get_report_path_uses_iso_date():
    path = get_report_path("reports", date(2026, 4, 24))
    assert path == Path("reports/2026-04-24.md")


def test_format_daily_report_contains_papers():
    body = format_daily_report(
        papers=[_make_paper()],
        report_date=date(2026, 4, 24),
        categories=["cs.AI"],
        keywords=["bug"],
    )
    assert "arXiv Daily Report - 2026-04-24" in body
    assert "`cs.AI`" in body
    assert "`bug`" in body
    assert "New papers: 1" in body
    assert "### 1. Test Paper" in body
    assert "This is a test abstract." in body


def test_format_daily_report_handles_no_papers():
    body = format_daily_report(
        papers=[],
        report_date=date(2026, 4, 24),
        categories=["cs.AI"],
        keywords=[],
    )
    assert "New papers: 0" in body
    assert "No new papers matched the configured filters today." in body
    assert "Keywords: all papers" in body


def test_write_daily_report_writes_markdown_file(tmp_path):
    report_path = write_daily_report(
        papers=[_make_paper()],
        report_dir=tmp_path,
        report_date=date(2026, 4, 24),
        categories=["cs.AI"],
        keywords=["bug"],
    )

    assert report_path == tmp_path / "2026-04-24.md"
    assert report_path.exists()
    assert "Test Paper" in report_path.read_text(encoding="utf-8")
