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
    path = get_archive_path("data/papers", _make_paper())
    assert path == Path("data/papers/2024-01-15_Test-Paper_2401.12345.md")


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

    assert saved_path == tmp_path / "2024-01-15_Test-Paper_2401.12345.md"
    assert saved_path.exists()
    assert "This is a test abstract." in saved_path.read_text(encoding="utf-8")
    assert is_already_archived(tmp_path, paper.source_id) is True


def test_filename_is_safe_and_bounded(tmp_path):
    from dataclasses import replace
    paper = replace(_make_paper(), title='../A/B: "title"? <test> ' + '論文' * 200)
    path = get_archive_path(tmp_path, paper)
    assert path.parent == tmp_path
    assert len(path.name.encode('utf-8')) < 255
    assert '/' not in path.name
    assert ':' not in path.name
    assert path.name.startswith('2024-01-15_')
    assert path.name.endswith('_2401.12345.md')


def test_dedup_uses_id_despite_changed_title_or_version(tmp_path):
    from dataclasses import replace
    archive_paper(_make_paper(), tmp_path)
    assert is_already_archived(tmp_path, '2401.12345v8')
    assert not is_already_archived(tmp_path, '2401.12346v1')
    other = replace(_make_paper(), source_id='2401.99999v1')
    assert get_archive_path(tmp_path, other) != get_archive_path(tmp_path, _make_paper())


def test_migration_preserves_content_and_legacy_dedup(tmp_path):
    from src.archive import migrate_archive, read_archive
    paper = _make_paper()
    old = tmp_path / '2401.12345.md'
    body = format_archive_markdown(paper)
    old.write_text(body, encoding='utf-8')
    assert is_already_archived(tmp_path, paper.source_id)
    assert migrate_archive(tmp_path) == 1
    new = get_archive_path(tmp_path, paper)
    assert new.read_text(encoding='utf-8') == body
    assert not old.exists()
    assert read_archive(new) == paper
    assert migrate_archive(tmp_path) == 0


def test_migration_refuses_collision_without_overwriting(tmp_path):
    import pytest
    from src.archive import migrate_archive
    paper = _make_paper()
    (tmp_path / '2401.12345.md').write_text(format_archive_markdown(paper))
    new = archive_paper(paper, tmp_path)
    with pytest.raises(FileExistsError):
        migrate_archive(tmp_path)
    assert new.exists()
    assert (tmp_path / '2401.12345.md').exists()
