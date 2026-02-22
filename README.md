# arxiv-issue-bot

Automatically create GitHub Issues for new arXiv papers in your research areas.

## How it works

A GitHub Actions workflow runs daily, queries the arXiv API for recent papers in your configured categories, filters by optional keywords, and creates a GitHub Issue for each new paper. Duplicate papers are never posted twice.

## Quick start

1. **Fork** this repository
2. Edit `config.yml` to set your categories and keywords
3. Enable GitHub Actions in your fork (Actions tab > "I understand my workflows, go ahead and enable them")
4. That's it -- the bot runs daily via GitHub Actions

You can also trigger it manually: **Actions** tab > **Fetch arXiv Papers** > **Run workflow**.

## Configuration

Edit `config.yml`:

```yaml
# arXiv categories to monitor
# Full list: https://arxiv.org/category_taxonomy
categories:
  - cs.AI
  - cs.SE

# Optional keyword filters (applied to title + abstract)
# If empty or omitted, ALL papers in the categories above are posted.
keywords:
  - "large language model"
  - "transformer"
  - "refactoring"
  - "agent"
  - "bug"
  - "defect"

# Maximum number of papers to fetch per category per run
max_results_per_category: 50

# Issue label prefix (categories become labels like "arxiv:cs.AI")
label_prefix: "arxiv"

# Whether to include cross-listed papers
include_cross_listed: true
```

## How deduplication works

- Each issue title contains the arXiv ID: `[2401.12345v1] Paper Title`
- Before creating an issue, the bot searches existing issues for the same base ID (version number stripped)
- Both open and closed issues are checked, so closing an issue won't cause duplicates

## Development

```bash
# Install dependencies
uv sync

# Run tests
uv run pytest

# Run locally (requires gh CLI authenticated)
uv run python -m src.main
```

## Extending

To add a new paper source (e.g., Semantic Scholar), implement the `PaperFetcher` interface in `src/fetcher.py`.

## License

MIT
