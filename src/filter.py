from src.fetcher import Paper


def filter_papers(papers: list[Paper], keywords: list[str]) -> list[Paper]:
    if not keywords:
        return papers
    keywords_lower = [kw.lower() for kw in keywords]
    return [
        p
        for p in papers
        if any(
            kw in p.title.lower() or kw in p.abstract.lower()
            for kw in keywords_lower
        )
    ]
