# arxiv-issue-bot

Automatically fetch new arXiv papers in your research areas and save their English abstracts into this repository.

## How it works

A GitHub Actions workflow runs daily, queries the arXiv API for recent papers in your configured categories, filters by optional keywords, saves each new paper as a Markdown file under `data/papers/`, and generates a daily summary report under `reports/`.

## Quick start

1. **Fork** this repository
2. Edit `config.yml` to set your categories and keywords
3. Enable GitHub Actions in your fork (Actions tab > "I understand my workflows, go ahead and enable them")
4. That's it -- the bot runs daily via GitHub Actions, commits new archives and reports back to your repo, and uploads the daily report as an Actions artifact

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

# Optional: issue label prefix when create_github_issues is true
label_prefix: "arxiv"

# Whether to include cross-listed papers
include_cross_listed: true

# Where to save archived paper summaries
archive_dir: "data/papers"

# Where to save daily summary reports
report_dir: "reports"

# Optional: also create GitHub Issues for new papers
create_github_issues: false
```

Each archived paper file contains paper metadata plus the original English abstract. Each daily report summarizes the newly discovered papers for that run.

## How deduplication works

- Each archive filename is based on the base arXiv ID, with the version suffix stripped
- Before saving, the bot checks whether that archive file already exists
- A daily report file is generated for each run date
- Optional GitHub issue creation still uses the same version-stripped ID check as before

## Development

```bash
# Install dependencies
python3 -m pip install .
python3 -m pip install pytest

# Run tests
python3 -m pytest

# Run locally
python3 -m src.main
```

## Extending

To add a new paper source (e.g., Semantic Scholar), implement the `PaperFetcher` interface in `src/fetcher.py`.

## License

MIT
