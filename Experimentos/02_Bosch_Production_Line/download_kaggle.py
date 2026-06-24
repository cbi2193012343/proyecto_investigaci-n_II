from __future__ import annotations

import sys
from pathlib import Path

import requests


ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from kaggle_common import download_from_kaggle, raw_data_dir


COMPETITION_SLUG = "bosch-production-line-performance"


def main() -> None:
    try:
        download_from_kaggle(
            competition=COMPETITION_SLUG,
            output_dir=raw_data_dir(__file__),
            unzip=True,
        )
    except requests.exceptions.HTTPError as exc:
        if getattr(exc.response, "status_code", None) == 403:
            print(
                "Bosch download blocked by Kaggle competition rules. "
                "Open the competition page in Kaggle and accept the rules "
                "with this account, then rerun this script.",
                file=sys.stderr,
            )
            raise SystemExit(1) from exc
        raise


if __name__ == "__main__":
    main()
