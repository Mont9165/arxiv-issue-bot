from dataclasses import replace
from datetime import date
from pathlib import Path
from urllib.parse import unquote
import re

from src.archive import archive_paper
from src.fetcher import Paper
from src.report import abstract_excerpt, format_daily_report, get_report_path, write_daily_report


def _make_paper() -> Paper:
    return Paper(
        source_id="2401.12345v1", title="Test Paper", authors=["Alice", "Bob"],
        abstract="This is a test abstract. More details that belong in the archive.",
        url="https://arxiv.org/abs/2401.12345v1",
        pdf_url="https://arxiv.org/pdf/2401.12345v1",
        categories=["cs.AI", "cs.SE"], primary_category="cs.AI", published="2024-01-15",
    )


def test_get_report_path_uses_iso_date():
    assert get_report_path("reports", date(2026, 4, 24)) == Path("reports/2026-04-24.md")


def test_report_is_concise_and_links_to_full_archive():
    body = format_daily_report([_make_paper()], date(2026, 4, 24), ["cs.AI"], ["bug"])
    assert "新着 1 件" in body
    assert "`cs.AI` 1 件" in body
    assert "`bug`" in body
    assert "2024-01-15" in body
    assert "This is a test abstract." in body
    assert "More details" not in body
    assert "../data/papers/2024-01-15_Test-Paper_2401.12345.md" in body


def test_report_empty_day():
    body = format_daily_report([], date(2026, 4, 24), ["cs.AI"], [])
    assert "新着 0 件" in body
    assert "今回、新たに見つかった対象論文はありません。" in body


def test_excerpt_is_bounded():
    assert len(abstract_excerpt("word " * 300)) <= 240
    assert abstract_excerpt("word " * 300).endswith("…")


def test_same_day_reruns_preserve_and_merge_papers(tmp_path):
    archives, reports = tmp_path / "papers", tmp_path / "reports"
    paper = _make_paper()
    archive_paper(paper, archives)
    kwargs = dict(report_dir=reports, report_date=date(2026, 4, 24),
                  categories=["cs.AI"], keywords=[], archive_dir=archives)
    path = write_daily_report([paper], **kwargs)
    original = path.read_text()
    write_daily_report([], **kwargs)
    assert path.read_text() == original
    other = replace(paper, source_id="2401.99999v1", title="Another Paper")
    archive_paper(other, archives)
    write_daily_report([other, replace(paper, source_id="2401.12345v2")], **kwargs)
    body = path.read_text()
    assert "新着 2 件" in body
    assert body.count("<!-- arxiv:2401.12345 -->") == 1
    assert (reports / "latest.md").read_text() == body
    for link in re.findall(r"\[詳細\]\(([^)]+)\)", body):
        assert (reports / unquote(link)).exists()


def test_legacy_report_is_preserved_on_first_run(tmp_path):
    archives, reports = tmp_path / "papers", tmp_path / "reports"
    archive_paper(_make_paper(), archives)
    reports.mkdir()
    path = reports / "2026-04-24.md"
    path.write_text("# Old report\n\n- arXiv ID: `2401.12345v1`\n")
    write_daily_report([], reports, date(2026, 4, 24), ["cs.AI"], [], archives)
    assert "Test Paper" in path.read_text()
    assert "新着 1 件" in path.read_text()


def test_actions_summary_has_absolute_links(tmp_path, monkeypatch):
    summary = tmp_path / "summary.md"
    monkeypatch.setenv("GITHUB_STEP_SUMMARY", str(summary))
    monkeypatch.setenv("GITHUB_REPOSITORY", "owner/repo")
    write_daily_report([_make_paper()], tmp_path / "reports", date(2026, 4, 24), [], [])
    assert "https://github.com/owner/repo/blob/HEAD/data/papers/" in summary.read_text()


def test_older_report_does_not_replace_latest(tmp_path):
    write_daily_report([], tmp_path, date(2026, 4, 25), [], [])
    latest = (tmp_path / "latest.md").read_text()
    write_daily_report([], tmp_path, date(2026, 4, 24), [], [])
    assert (tmp_path / "latest.md").read_text() == latest
