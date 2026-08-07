from pathlib import Path

from src.archive import (
    archive_paper,
    format_archive_markdown,
    get_archive_path,
    is_already_archived,
)
from src.fetcher import Paper


def _make_paper() -> Paper:
    return Paper(
        source_id="2401.12345v2",
        title="Test Paper",
        authors=["Alice", "Bob"],
        abstract="This is a test abstract.",
        url="https://arxiv.org/abs/2401.12345v2",
        pdf_url="https://arxiv.org/pdf/2401.12345v2",
        categories=["cs.AI", "cs.SE"],
        primary_category="cs.AI",
        published="2024-01-15",
    )


def test_get_archive_path_uses_base_id():
    path = get_archive_path("data/papers", "2401.12345v2")
    assert path == Path("data/papers/2401.12345.md")


def test_format_archive_markdown_contains_key_info():
    paper = _make_paper()
    body = format_archive_markdown(paper)
    assert "# Test Paper" in body
    assert "2401.12345v2" in body
    assert "Alice, Bob" in body
    assert "2024-01-15" in body
    assert "`cs.AI`" in body
    assert "[abs]" in body
    assert "[pdf]" in body
    assert "This is a test abstract." in body


def test_archive_paper_writes_markdown_file(tmp_path):
    paper = _make_paper()
    saved_path = archive_paper(paper, tmp_path)

    assert saved_path == tmp_path / "2401.12345.md"
    assert saved_path.exists()
    assert "This is a test abstract." in saved_path.read_text(encoding="utf-8")
    assert is_already_archived(tmp_path, paper.source_id) is True
