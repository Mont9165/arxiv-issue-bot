import sys
import time
from datetime import date

from src.archive import archive_paper, is_already_archived
from src.config import load_config
from src.fetcher import ArxivFetcher, Paper
from src.filter import filter_papers
from src.issue_manager import create_issue, is_already_posted, normalize_arxiv_id
from src.report import write_daily_report


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

    new_papers = [
        p for p in filtered if not is_already_archived(config.archive_dir, p.source_id)
    ]
    print(f"New papers (not yet archived): {len(new_papers)}")

    report_path = write_daily_report(
        papers=new_papers,
        report_dir=config.report_dir,
        report_date=date.today(),
        categories=config.categories,
        keywords=config.keywords,
    )
    print(f"Daily report: {report_path}")

    archived = 0
    created = 0
    for paper in new_papers:
        archive_path = archive_paper(paper, config.archive_dir)
        archived += 1
        print(f"  Archived: [{paper.source_id}] {archive_path}")

        if not config.create_github_issues:
            continue

        if is_already_posted(paper.source_id):
            print(f"  Skipped issue: [{paper.source_id}] already exists")
            continue

        if create_issue(paper, config.label_prefix):
            created += 1
            print(f"  Created issue: [{paper.source_id}] {paper.title}")
        else:
            print(
                f"  FAILED issue:  [{paper.source_id}] {paper.title}",
                file=sys.stderr,
            )

    print(
        f"\nDone. Archived {archived} new papers"
        f" and created {created} new issues."
    )


if __name__ == "__main__":
    main()
