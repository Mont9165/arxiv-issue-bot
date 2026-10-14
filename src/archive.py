from datetime import date
from pathlib import Path
import re
import unicodedata

from src.fetcher import Paper
from src.identifiers import normalize_arxiv_id


def get_archive_path(archive_dir: str | Path, paper: Paper) -> Path:
    base_id = normalize_arxiv_id(paper.source_id)
    safe_name = base_id.replace("/", "_")
    if not re.fullmatch(r"[\w.-]+", safe_name):
        raise ValueError(f"Invalid arXiv ID: {paper.source_id}")
    published = date.fromisoformat(paper.published).isoformat()
    title = unicodedata.normalize("NFKC", paper.title)
    title = re.sub(r"[^\w-]+", "-", title).strip("-_")
    # Leave room for the date, ID and extension, even with multibyte titles.
    title = title.encode("utf-8")[:160].decode("utf-8", errors="ignore").rstrip("-_")
    return Path(archive_dir) / f"{published}_{title or 'Untitled'}_{safe_name}.md"


def is_already_archived(archive_dir: str | Path, arxiv_id: str) -> bool:
    safe_id = normalize_arxiv_id(arxiv_id).replace("/", "_")
    directory = Path(archive_dir)
    return (directory / f"{safe_id}.md").exists() or any(
        path.name.endswith(f"_{safe_id}.md") for path in directory.glob("*.md")
    )


def read_archive(path: Path) -> Paper:
    """Read the original archive format as well as newly named archives."""
    text = path.read_text(encoding="utf-8")
    header, abstract = text.split("\n## Abstract\n", 1)
    metadata = dict(re.findall(r"^- ([^:]+): (.*)$", header, re.MULTILINE))
    links = dict(re.findall(r"\[(abs|pdf)\]\(([^)]+)\)", metadata["Links"]))
    return Paper(
        source_id=metadata["arXiv ID"].strip("`"),
        title=header.splitlines()[0].removeprefix("# "),
        authors=metadata["Authors"].split(", "),
        abstract=abstract.strip(),
        url=links["abs"],
        pdf_url=links.get("pdf"),
        categories=re.findall(r"`([^`]+)`", metadata["Categories"]),
        primary_category=metadata["Primary category"].strip("`"),
        published=metadata["Published"],
    )


def load_archive(archive_dir: str | Path) -> dict[str, Paper]:
    papers = {}
    for path in sorted(Path(archive_dir).glob("*.md")):
        paper = read_archive(path)
        base_id = normalize_arxiv_id(paper.source_id)
        if base_id in papers:
            raise ValueError(f"Duplicate archive for {base_id}")
        papers[base_id] = paper
    return papers


def migrate_archive(archive_dir: str | Path) -> int:
    """Rename existing files without changing their contents or overwriting files."""
    renames = []
    for path in sorted(Path(archive_dir).glob("*.md")):
        target = get_archive_path(archive_dir, read_archive(path))
        if path != target:
            if target.exists():
                raise FileExistsError(target)
            renames.append((path, target))
    if len({target for _, target in renames}) != len(renames):
        raise ValueError("Archive migration has conflicting target filenames")
    for path, target in renames:
        path.rename(target)
    return len(renames)


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
    path = get_archive_path(archive_dir, paper)
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(".md.tmp")
    temporary.write_text(format_archive_markdown(paper), encoding="utf-8")
    temporary.replace(path)
    return path
