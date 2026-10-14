from src.identifiers import normalize_arxiv_id


def test_normalize_arxiv_id_removes_version():
    assert normalize_arxiv_id("2401.12345v1") == "2401.12345"
    assert normalize_arxiv_id("2401.12345v10") == "2401.12345"
    assert normalize_arxiv_id("hep-th/9901001v2") == "hep-th/9901001"


def test_normalize_arxiv_id_no_version():
    assert normalize_arxiv_id("2401.12345") == "2401.12345"
