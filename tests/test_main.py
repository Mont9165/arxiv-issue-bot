from dataclasses import replace
from pathlib import Path

from src.config import Config
import src.main as app
from tests.test_report import _make_paper


def test_main_archives_once_and_preserves_report_on_rerun(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    config = Config(categories=['cs.AI', 'cs.SE'], keywords=[])
    monkeypatch.setattr(app, 'load_config', lambda: config)
    monkeypatch.setattr(app.time, 'sleep', lambda _: None)
    paper = _make_paper()

    class Fetcher:
        def fetch(self, category, max_results):
            return [paper, replace(paper, source_id='2401.12345v2')]

    monkeypatch.setattr(app, 'ArxivFetcher', Fetcher)
    monkeypatch.setenv('GITHUB_OUTPUT', str(tmp_path / 'outputs'))
    app.main()
    files = list(Path('data/papers').glob('*.md'))
    assert len(files) == 1
    assert files[0].name == '2024-01-15_Test-Paper_2401.12345.md'
    first = Path('reports/latest.md').read_text()
    app.main()
    assert len(list(Path('data/papers').glob('*.md'))) == 1
    assert Path('reports/latest.md').read_text() == first
    assert 'report_path=reports/' in (tmp_path / 'outputs').read_text()


def test_main_recovers_if_archive_write_fails(tmp_path, monkeypatch):
    import pytest
    from src.archive import archive_paper
    monkeypatch.chdir(tmp_path)
    monkeypatch.setattr(app, 'load_config', lambda: Config(categories=['cs.AI']))
    paper = _make_paper()

    class Fetcher:
        def fetch(self, category, max_results):
            return [paper]

    monkeypatch.setattr(app, 'ArxivFetcher', Fetcher)

    def fail(*args):
        raise OSError('Disk full')

    monkeypatch.setattr(app, 'archive_paper', fail)
    with pytest.raises(OSError):
        app.main()
    monkeypatch.setattr(app, 'archive_paper', archive_paper)
    app.main()
    assert len(list(Path('data/papers').glob('*.md'))) == 1
    assert '新着 1 件' in Path('reports/latest.md').read_text()
