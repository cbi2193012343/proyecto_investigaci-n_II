from __future__ import annotations

import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from kaggle_common import download_from_kaggle, raw_data_dir


# Better fit for the finance extension in the manuscript:
# daily 2000-2026 market regimes with an explicit Crisis label and macro data.
DATASET_SLUG = "mafaqbhatti/stock-market-regimes-20002026"


def main() -> None:
    download_from_kaggle(
        dataset=DATASET_SLUG,
        output_dir=raw_data_dir(__file__),
        unzip=True,
    )


if __name__ == "__main__":
    main()
