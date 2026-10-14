import os
import time
from datetime import datetime, timezone
from pathlib import Path

from src.archive import archive_paper, load_archive, migrate_archive
from src.config import load_config
from src.fetcher import ArxivFetcher, Paper
from src.filter import filter_papers
from src.identifiers import normalize_arxiv_id
from src.report import write_daily_report


def main() -> None:
    config = load_config()
    report_date = datetime.now(timezone.utc).date()
    migrate_archive(config.archive_dir)
    existing = load_archive(config.archive_dir)
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
        p for p in filtered if normalize_arxiv_id(p.source_id) not in existing
    ]
    print(f"New papers (not yet archived): {len(new_papers)}")

    # Write the report first: a failed archive write can be recovered on retry
    # without losing the IDs discovered in this run.
    report_path = write_daily_report(
        papers=new_papers,
        report_dir=config.report_dir,
        report_date=report_date,
        categories=config.categories,
        keywords=config.keywords,
        archive_dir=config.archive_dir,
    )
    print(f"Daily report: {report_path}")

    archived = 0
    for paper in new_papers:
        archive_path = archive_paper(paper, config.archive_dir)
        archived += 1
        print(f"  Archived: [{paper.source_id}] {archive_path}")

    if output := os.environ.get("GITHUB_OUTPUT"):
        with Path(output).open("a", encoding="utf-8") as stream:
            stream.write(f"report_path={report_path}\n")

    print(f"\nDone. Archived {archived} new papers.")


if __name__ == "__main__":
    main()
