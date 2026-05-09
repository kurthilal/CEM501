from __future__ import annotations

import logging
from pathlib import Path


def setup_logging(*, log_path: str | Path, verbose: bool = False) -> None:
    path = Path(log_path)
    path.parent.mkdir(parents=True, exist_ok=True)

    level = logging.DEBUG if verbose else logging.INFO
    fmt = "%(asctime)s | %(levelname)s | %(name)s | %(message)s"

    logging.basicConfig(level=level, format=fmt, handlers=[logging.FileHandler(path), logging.StreamHandler()])

