import yaml
from dataclasses import dataclass, field
from pathlib import Path


@dataclass
class Config:
    categories: list[str]
    keywords: list[str] = field(default_factory=list)
    max_results_per_category: int = 50
    label_prefix: str = "arxiv"
    include_cross_listed: bool = True


def load_config(path: str = "config.yml") -> Config:
    with open(path) as f:
        raw = yaml.safe_load(f)
    if not raw or not raw.get("categories"):
        raise ValueError("config.yml must specify at least one category")
    return Config(
        **{k: v for k, v in raw.items() if k in Config.__dataclass_fields__}
    )
