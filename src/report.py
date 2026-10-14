from collections import Counter
from datetime import date
import os
from pathlib import Path
import re
import textwrap
from urllib.parse import quote

from src.archive import get_archive_path, load_archive
from src.fetcher import Paper
from src.identifiers import normalize_arxiv_id


def get_report_path(report_dir: str | Path, report_date: date) -> Path:
    return Path(report_dir) / f"{report_date.isoformat()}.md"


def abstract_excerpt(abstract: str, width: int = 240) -> str:
    """A short extract from the original abstract; no generated claims."""
    text = " ".join(abstract.split())
    first_sentence = re.split(r"(?<=[.!?])\s+(?=[A-Z])", text, maxsplit=1)[0]
    return textwrap.shorten(first_sentence, width=width, placeholder="…")


def escape_markdown(text: str) -> str:
    return re.sub(r"([\\`*_{}\[\]<>|])", r"\\\1", text)


def format_daily_report(
    papers: list[Paper],
    report_date: date,
    categories: list[str],
    keywords: list[str],
    archive_dir: str | Path = "data/papers",
    report_dir: str | Path = "reports",
    repository_url: str | None = None,
) -> str:
    papers = sorted(papers, key=lambda p: (p.published, p.source_id), reverse=True)
    lines = [
        f"# arXiv デイリーサマリー — {report_date.isoformat()}",
        "",
        f"**新着 {len(papers)} 件**（UTC の収集日基準。公開日は各項目に記載）",
        "",
        f"- 対象分野: {', '.join(f'`{category}`' for category in categories)}",
        f"- キーワード: {', '.join(f'`{keyword}`' for keyword in keywords) if keywords else '指定なし'}",
    ]
    counts = Counter(p.primary_category for p in papers)
    if counts:
        lines.append("- 主分野別: " + "、".join(
            f"`{category}` {count} 件" for category, count in sorted(counts.items())
        ))
    lines.append("")
    if not papers:
        lines.append("今回、新たに見つかった対象論文はありません。")
    else:
        lines.extend(["各項目は原文の要旨冒頭の短い抜粋です。全文は「詳細」から読めます。", ""])
        for paper in papers:
            archive_path = get_archive_path(archive_dir, paper)
            if repository_url:
                detail_url = f"{repository_url}/blob/HEAD/{quote(archive_path.as_posix())}"
            else:
                detail_url = quote(Path(os.path.relpath(archive_path, report_dir)).as_posix())
            lines.extend([
                f"<!-- arxiv:{normalize_arxiv_id(paper.source_id)} -->",
                f"- **[{escape_markdown(paper.title)}]({paper.url})** "
                f"（{paper.published} / `{paper.primary_category}`） "
                f"[詳細]({detail_url})",
                f"  {escape_markdown(abstract_excerpt(paper.abstract))}",
                "",
            ])
    return "\n".join(lines).rstrip() + "\n"


def write_daily_report(
    papers: list[Paper],
    report_dir: str | Path,
    report_date: date,
    categories: list[str],
    keywords: list[str],
    archive_dir: str | Path = "data/papers",
) -> Path:
    path = get_report_path(report_dir, report_date)
    path.parent.mkdir(parents=True, exist_ok=True)
    combined = {}
    if path.exists():
        previous = path.read_text(encoding="utf-8")
        # Accept both the original full-abstract reports and the concise format.
        previous_ids = re.findall(
            r"<!-- arxiv:([^ ]+) -->|^- arXiv ID: `([^`]+)`", previous, re.MULTILINE
        )
        archived = load_archive(archive_dir)
        incoming = {normalize_arxiv_id(p.source_id): p for p in papers}
        for new_id, legacy_id in previous_ids:
            base_id = normalize_arxiv_id(new_id or legacy_id)
            paper = incoming.get(base_id) or archived.get(base_id)
            if paper is None:
                raise ValueError(f"Cannot preserve daily report: missing archive {base_id}")
            combined[base_id] = paper
    for paper in papers:
        combined[normalize_arxiv_id(paper.source_id)] = paper
    kwargs = dict(
        papers=list(combined.values()), report_date=report_date,
        categories=categories, keywords=keywords,
        archive_dir=archive_dir, report_dir=report_dir,
    )
    body = format_daily_report(**kwargs)
    # Replace atomically so an interrupted write does not erase the day's report.
    temporary = path.with_suffix(".md.tmp")
    temporary.write_text(body, encoding="utf-8")
    temporary.replace(path)
    dated_reports = sorted(Path(report_dir).glob("????-??-??.md"))
    if dated_reports[-1] == path:
        (Path(report_dir) / "latest.md").write_text(body, encoding="utf-8")
    if summary := os.environ.get("GITHUB_STEP_SUMMARY"):
        repository = os.environ.get("GITHUB_REPOSITORY")
        server = os.environ.get("GITHUB_SERVER_URL", "https://github.com")
        url = f"{server}/{repository}" if repository else None
        with Path(summary).open("a", encoding="utf-8") as stream:
            stream.write(format_daily_report(**kwargs, repository_url=url))
    return path
