import json
import re
import subprocess

from src.fetcher import Paper


def normalize_arxiv_id(arxiv_id: str) -> str:
    return re.sub(r"v\d+$", "", arxiv_id)


def is_already_posted(arxiv_id: str) -> bool:
    base_id = normalize_arxiv_id(arxiv_id)
    result = subprocess.run(
        [
            "gh",
            "search",
            "issues",
            f"[{base_id}] in:title",
            "--json",
            "title",
            "--limit",
            "5",
        ],
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        return False
    issues = json.loads(result.stdout)
    for issue in issues:
        title = issue.get("title", "")
        if title.startswith("[") and "]" in title:
            existing_id = title[1 : title.index("]")]
            if normalize_arxiv_id(existing_id) == base_id:
                return True
    return False


def ensure_label_exists(label: str) -> None:
    subprocess.run(
        [
            "gh",
            "label",
            "create",
            label,
            "--description",
            f"arXiv category: {label}",
            "--force",
        ],
        capture_output=True,
        text=True,
    )


def format_issue_body(paper: Paper) -> str:
    authors_str = ", ".join(paper.authors)
    categories_str = ", ".join(f"`{c}`" for c in paper.categories)
    links = f"[abs]({paper.url})"
    if paper.pdf_url:
        links += f" | [pdf]({paper.pdf_url})"
    return (
        f"## {paper.title}\n\n"
        f"**Authors:** {authors_str}\n"
        f"**Published:** {paper.published}\n"
        f"**Categories:** {categories_str}\n\n"
        f"**Links:** {links}\n\n"
        f"---\n\n"
        f"### Abstract\n\n"
        f"{paper.abstract}\n"
    )


def create_issue(paper: Paper, label_prefix: str) -> bool:
    title = f"[{paper.source_id}] {paper.title}"
    labels = [f"{label_prefix}:{cat}" for cat in paper.categories]

    for label in labels:
        ensure_label_exists(label)

    body = format_issue_body(paper)

    result = subprocess.run(
        [
            "gh",
            "issue",
            "create",
            "--title",
            title,
            "--body",
            body,
            "--label",
            ",".join(labels),
        ],
        capture_output=True,
        text=True,
    )
    return result.returncode == 0
