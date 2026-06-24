from __future__ import annotations

import os
import zipfile
from pathlib import Path


def project_root(script_file: str | Path) -> Path:
    """Return the repository root for a script inside Experimentos/*."""
    return Path(script_file).resolve().parents[2]


def raw_data_dir(script_file: str | Path) -> Path:
    """Standard raw-data folder for one experiment."""
    return Path(script_file).resolve().parent / "data" / "raw"


def _candidate_token_files(script_file: str | Path) -> list[Path]:
    script_path = Path(script_file).resolve()
    candidates: list[Path] = []

    for parent in [script_path, *script_path.parents]:
        candidates.extend(
            [
                parent / ".kaggle" / "access_token",
                parent / ".kaggle" / "access_token.txt",
                parent / ".kaggle" / "kaggle.json",
            ]
        )

    candidates.extend(
        [
            Path.home() / ".kaggle" / "access_token",
            Path.home() / ".kaggle" / "access_token.txt",
            Path.home() / ".kaggle" / "kaggle.json",
        ]
    )
    return candidates


def configure_kaggle_auth(script_file: str | Path) -> None:
    """Populate Kaggle auth from local files when the environment is empty."""
    if os.environ.get("KAGGLE_API_TOKEN"):
        return

    for candidate in _candidate_token_files(script_file):
        if not candidate.is_file():
            continue

        content = candidate.read_text(encoding="utf-8").strip()
        if not content:
            continue

        if candidate.name == "kaggle.json":
            # Legacy credentials file used by the Kaggle API client.
            os.environ.setdefault("KAGGLE_CONFIG_DIR", str(candidate.parent))
        else:
            # Newer token-based auth used by kagglehub / Kaggle CLI 2.x.
            os.environ["KAGGLE_API_TOKEN"] = content
        return


def download_from_kaggle(
    *,
    output_dir: str | Path,
    dataset: str | None = None,
    competition: str | None = None,
    unzip: bool = True,
    force: bool = True,
    quiet: bool = False,
) -> Path:
    """Download a Kaggle dataset or competition into output_dir.

    Requires the Kaggle CLI credentials to be available on the machine
    (usually ~/.kaggle/kaggle.json or equivalent environment config).
    """
    if bool(dataset) == bool(competition):
        raise ValueError("Provide exactly one of dataset or competition.")

    configure_kaggle_auth(Path(output_dir))

    try:
        import truststore

        truststore.inject_into_ssl()
    except Exception:
        # If truststore is unavailable or fails, fall back to the default SSL setup.
        pass

    try:
        from kaggle.api.kaggle_api_extended import KaggleApi
    except ImportError as exc:  # pragma: no cover - runtime dependency
        raise SystemExit(
            "Missing dependency: kaggle. Install it with `pip install kaggle`."
        ) from exc

    target_dir = Path(output_dir)
    target_dir.mkdir(parents=True, exist_ok=True)

    api = KaggleApi()
    api.authenticate()

    if dataset:
        api.dataset_download_files(
            dataset,
            path=str(target_dir),
            force=force,
            quiet=quiet,
            unzip=unzip,
        )
    else:
        api.competition_download_files(
            competition,
            path=str(target_dir),
            force=force,
            quiet=quiet,
        )
        if unzip:
            for archive in target_dir.glob("*.zip"):
                with zipfile.ZipFile(archive) as zf:
                    zf.extractall(target_dir)

    return target_dir
