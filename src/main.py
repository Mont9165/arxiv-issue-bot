import sys
import time

from src.config import load_config
from src.fetcher import ArxivFetcher, Paper
from src.filter import filter_papers
from src.issue_manager import create_issue, is_already_posted, normalize_arxiv_id


def main() -> None:
    config = load_config()
    fetcher = ArxivFetcher()

    all_papers: dict[str, Paper] = {}
    for i, category in enumerate(config.categories):
        if i > 0:
            time.sleep(3)
        papers = fetcher.fetch(category, config.max_results_per_category)
        for p in papers:
            if not config.include_cross_listed and p.primary_category != category:
                continue
            base_id = normalize_arxiv_id(p.source_id)
            if base_id not in all_papers:
                all_papers[base_id] = p

    print(
        f"Fetched {len(all_papers)} unique papers "
        f"across {len(config.categories)} categories"
    )

    filtered = filter_papers(list(all_papers.values()), config.keywords)
    print(f"After keyword filtering: {len(filtered)} papers")

    new_papers = [p for p in filtered if not is_already_posted(p.source_id)]
    print(f"New papers (not yet posted): {len(new_papers)}")

    created = 0
    for paper in new_papers:
        if create_issue(paper, config.label_prefix):
            created += 1
            print(f"  Created: [{paper.source_id}] {paper.title}")
        else:
            print(
                f"  FAILED:  [{paper.source_id}] {paper.title}",
                file=sys.stderr,
            )

    print(f"\nDone. Created {created} new issues.")


if __name__ == "__main__":
    main()
