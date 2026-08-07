from src.config import load_config


def test_load_config_uses_archive_defaults(tmp_path):
    config_path = tmp_path / "config.yml"
    config_path.write_text(
        "categories:\n"
        "  - cs.AI\n",
        encoding="utf-8",
    )

    config = load_config(str(config_path))

    assert config.categories == ["cs.AI"]
    assert config.archive_dir == "data/papers"
    assert config.create_github_issues is False
