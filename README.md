# arxiv-issue-bot

Automatically collect new arXiv papers in your research areas, archive their original English abstracts as Markdown, and publish a concise daily digest. No GitHub Issues are created.

**[Latest daily summary](reports/latest.md)** · [Daily reports](reports/) · [Paper archive](data/papers/)

## How it works

The GitHub Actions workflow runs every day at **09:00 UTC** (18:00 JST). It fetches recent papers in the configured categories, applies keyword filters, and commits the new files back to the repository.

- `data/papers/YYYY-MM-DD_Title_arxiv-id.md`: one paper per file, with its publication date, title, authors, categories, source links, and full original abstract. For example: `2026-10-13_RT-J-Large-Scale-Pretraining-of-Relational-Transformers-for-Context-Efficient-Predictions_2610.17867.md`.
- `reports/YYYY-MM-DD.md`: papers first discovered on that UTC collection date, with counts by primary category, titles, publication dates, and short excerpts from the original English abstracts (up to 240 characters each). These are extracts, not AI-generated or translated summaries.
- `reports/latest.md`: the most recent daily report. The same report is displayed in the Actions run summary and uploaded as an artifact.

The date in a **paper filename is its arXiv publication date**; the date in a **report filename is its collection date**. A report can include papers published on earlier days. arXiv publication does not necessarily mean peer-reviewed publication.

## Quick start

1. Fork this repository.
2. Edit `config.yml` to set your categories and keywords.
3. Enable GitHub Actions in your fork.
4. Read [the latest summary](reports/latest.md) after each daily run.

You can also trigger it manually: **Actions → Fetch arXiv Papers → Run workflow**. The workflow needs `contents: write` to commit its results; no issue permissions, GitHub CLI token, or external summarization API key are needed.

## Configuration

```yaml
categories:
  - cs.DB
  - cs.SE

# Match ANY keyword in the title or abstract. Empty means all papers.
keywords:
  - "semantic"
  - "database"
  - "large language model"

max_results_per_category: 50
include_cross_listed: true
archive_dir: "data/papers"
report_dir: "reports"
```

The fetch limit applies per category per run. The digest describes newly discovered papers within that fetched set, not every paper published on arXiv. If a category is busy or runs are missed, raise the limit to avoid missing papers. If you change the output directories, also update the workflow's commit paths.

## Filenames and deduplication

- Filenames use the publication date, a filesystem-safe title, and the base arXiv ID to avoid collisions. Long titles are shortened in filenames; the complete title stays in the document.
- Existing ID-only archives are automatically renamed without changing their contents.
- Deduplication uses the version-stripped arXiv ID regardless of the filename or title. New versions of an archived paper are not treated as new papers.
- Re-running on the same day preserves earlier results and merges newly found papers. Empty days still produce a report.
- Existing full-length daily reports remain readable; a report is converted to the concise format when that date is regenerated.

## Development

```bash
python3 -m pip install .
python3 -m pip install pytest
python3 -m pytest
python3 -m src.main
```

A local run fetches papers and writes archives and reports; committing is handled separately by the workflow.

## Extending

To add a new paper source, implement the `PaperFetcher` interface in `src/fetcher.py`.

## License

MIT
