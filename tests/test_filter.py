from src.fetcher import Paper
from src.filter import filter_papers


def _make_paper(title: str = "Test", abstract: str = "Nothing") -> Paper:
    return Paper(
        source_id="2401.00001v1",
        title=title,
        authors=["Author"],
        abstract=abstract,
        url="https://arxiv.org/abs/2401.00001v1",
        pdf_url="https://arxiv.org/pdf/2401.00001v1",
        categories=["cs.AI"],
        primary_category="cs.AI",
        published="2024-01-01",
    )


def test_no_keywords_returns_all():
    papers = [_make_paper(), _make_paper()]
    result = filter_papers(papers, [])
    assert len(result) == 2


def test_keyword_match_in_title():
    p = _make_paper(title="A Large Language Model for Code")
    result = filter_papers([p], ["large language model"])
    assert len(result) == 1


def test_keyword_match_in_abstract():
    p = _make_paper(abstract="We propose a novel transformer architecture.")
    result = filter_papers([p], ["transformer"])
    assert len(result) == 1


def test_keyword_no_match():
    p = _make_paper(title="Sorting algorithms", abstract="Bubble sort is slow.")
    result = filter_papers([p], ["transformer"])
    assert len(result) == 0


def test_keyword_case_insensitive():
    p = _make_paper(title="TRANSFORMER Networks")
    result = filter_papers([p], ["transformer"])
    assert len(result) == 1


def test_multiple_keywords_any_match():
    p1 = _make_paper(title="Transformer model")
    p2 = _make_paper(title="Reinforcement learning")
    p3 = _make_paper(title="Graph neural network")
    result = filter_papers([p1, p2, p3], ["transformer", "reinforcement"])
    assert len(result) == 2
