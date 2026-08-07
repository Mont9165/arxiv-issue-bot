from datetime import date
from pathlib import Path

from src.fetcher import Paper


def get_report_path(report_dir: str | Path, report_date: date) -> Path:
    return Path(report_dir) / f"{report_date.isoformat()}.md"


def format_daily_report(
    papers: list[Paper],
    report_date: date,
    categories: list[str],
    keywords: list[str],
) -> str:
    lines = [
        f"# arXiv Daily Report - {report_date.isoformat()}",
        "",
        f"- Categories: {', '.join(f'`{category}`' for category in categories)}",
        (
            f"- Keywords: {', '.join(f'`{keyword}`' for keyword in keywords)}"
            if keywords
            else "- Keywords: all papers"
        ),
        f"- New papers: {len(papers)}",
        "",
    ]

    if not papers:
        lines.extend(
            [
                "## Summary",
                "",
                "No new papers matched the configured filters today.",
            ]
        )
        return "\n".join(lines) + "\n"

    lines.extend(["## Papers", ""])
    for index, paper in enumerate(papers, start=1):
        links = f"[abs]({paper.url})"
        if paper.pdf_url:
            links += f" | [pdf]({paper.pdf_url})"
        authors = ", ".join(paper.authors)
        categories_str = ", ".join(f"`{category}`" for category in paper.categories)
        lines.extend(
            [
                f"### {index}. {paper.title}",
                "",
                f"- arXiv ID: `{paper.source_id}`",
                f"- Authors: {authors}",
                f"- Published: {paper.published}",
                f"- Categories: {categories_str}",
                f"- Links: {links}",
                "",
                paper.abstract.strip(),
                "",
            ]
        )

    return "\n".join(lines)


def write_daily_report(
    papers: list[Paper],
    report_dir: str | Path,
    report_date: date,
    categories: list[str],
    keywords: list[str],
) -> Path:
    path = get_report_path(report_dir, report_date)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        format_daily_report(papers, report_date, categories, keywords),
        encoding="utf-8",
    )
    return path
