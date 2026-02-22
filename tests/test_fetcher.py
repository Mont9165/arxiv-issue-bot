from unittest.mock import MagicMock, patch
from datetime import datetime

from src.fetcher import ArxivFetcher, Paper


def _mock_arxiv_result():
    result = MagicMock()
    result.get_short_id.return_value = "2401.12345v1"
    result.title = "Test Paper Title"
    result.authors = [MagicMock(name="Alice"), MagicMock(name="Bob")]
    result.authors[0].name = "Alice"
    result.authors[1].name = "Bob"
    result.summary = "This is the abstract."
    result.entry_id = "https://arxiv.org/abs/2401.12345v1"
    result.pdf_url = "https://arxiv.org/pdf/2401.12345v1"
    result.categories = ["cs.AI", "cs.LG"]
    result.primary_category = "cs.AI"
    result.published = datetime(2024, 1, 15)
    return result


@patch("src.fetcher.arxiv.Client")
def test_arxiv_fetcher_returns_papers(mock_client_cls):
    mock_client = MagicMock()
    mock_client_cls.return_value = mock_client
    mock_client.results.return_value = [_mock_arxiv_result()]

    fetcher = ArxivFetcher()
    papers = fetcher.fetch("cs.AI", max_results=10)

    assert len(papers) == 1
    p = papers[0]
    assert isinstance(p, Paper)
    assert p.source_id == "2401.12345v1"
    assert p.title == "Test Paper Title"
    assert p.authors == ["Alice", "Bob"]
    assert p.published == "2024-01-15"
    assert p.primary_category == "cs.AI"


@patch("src.fetcher.arxiv.Client")
def test_arxiv_fetcher_empty_results(mock_client_cls):
    mock_client = MagicMock()
    mock_client_cls.return_value = mock_client
    mock_client.results.return_value = []

    fetcher = ArxivFetcher()
    papers = fetcher.fetch("cs.AI", max_results=10)

    assert papers == []
