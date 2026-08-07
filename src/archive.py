from pathlib import Path

from src.fetcher import Paper
from src.issue_manager import normalize_arxiv_id


def get_archive_path(archive_dir: str | Path, arxiv_id: str) -> Path:
    base_id = normalize_arxiv_id(arxiv_id)
    safe_name = base_id.replace("/", "_")
    return Path(archive_dir) / f"{safe_name}.md"


def is_already_archived(archive_dir: str | Path, arxiv_id: str) -> bool:
    return get_archive_path(archive_dir, arxiv_id).exists()


def format_archive_markdown(paper: Paper) -> str:
    authors_str = ", ".join(paper.authors)
    categories_str = ", ".join(f"`{c}`" for c in paper.categories)
    links = f"[abs]({paper.url})"
    if paper.pdf_url:
        links += f" | [pdf]({paper.pdf_url})"

    return (
        f"# {paper.title}\n\n"
        f"- arXiv ID: `{paper.source_id}`\n"
        f"- Authors: {authors_str}\n"
        f"- Published: {paper.published}\n"
        f"- Primary category: `{paper.primary_category}`\n"
        f"- Categories: {categories_str}\n"
        f"- Links: {links}\n\n"
        f"## Abstract\n\n"
        f"{paper.abstract.strip()}\n"
    )


def archive_paper(paper: Paper, archive_dir: str | Path) -> Path:
    path = get_archive_path(archive_dir, paper.source_id)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(format_archive_markdown(paper), encoding="utf-8")
    return path
