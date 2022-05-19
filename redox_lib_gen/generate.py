#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pathlib import Path
from shutil import copy
from typing import List

import click
from gen_helpers import download_and_extract, format_python_files, process_files, rmrf
from requests import HTTPError

SPEC_URL = "https://developer.redoxengine.com/data-models/schemas.zip"
PARENT_DIR = Path(__file__).parent.resolve()
CACHE_DIR = PARENT_DIR / "cache"
LIB_DEST_DIR = (PARENT_DIR / ".." / ".." / "pyredox" / "pyredox").resolve()
TEMPLATE_DIR = PARENT_DIR / "templates"
DEFAULT_DIRS_TO_GENERATE = ["patientadmin", "scheduling"]


@click.command()
@click.option(
    "--dst",
    "-d",
    default=LIB_DEST_DIR,
    show_default=True,
    type=click.Path(
        file_okay=False, dir_okay=True, writable=True, resolve_path=True, path_type=Path
    ),
    help=(
        "The directory where the pyredox library will be generated. NOTE: If the "
        "provided path already exists, it will be deleted (along with its contents) "
        "before the library is generated or saved there."
    ),
)
@click.option(
    "--cache-dir",
    "-c",
    default=CACHE_DIR,
    type=click.Path(
        file_okay=False, dir_okay=True, writable=True, resolve_path=True, path_type=Path
    ),
    help=(
        "The directory where the Redox schema will downloaded and extracted. Any files "
        "in the directory will be overwritten."
    ),
)
@click.option("--spec_url", default=SPEC_URL, show_default=True, type=click.STRING)
@click.option(
    "--force-download",
    "-f",
    is_flag=True,
    help=(
        "Force a fresh download of the Redox specification zip file. If not specified "
        "and the zip file has already been downloaded, the local copy will be used "
        "instead of downloading a fresh version of the spec."
    ),
)
@click.argument("directories", nargs=-1)
def main(
    dst: Path,
    cache_dir: Path,
    spec_url: str,
    force_download: bool,
    directories: List[str],
):
    """Generate Pydantic models from the JSON specs in DIRECTORIES.

    DIRECTORIES is a list of directories that exist in the extracted spec
    archive that should be included in the generated output.
    """

    cache_dir.mkdir(exist_ok=True)
    try:
        extracted_folder = download_and_extract(spec_url, cache_dir, force_download)
    except HTTPError:
        click.echo(
            "Unable to download the spec from Redox. This happens somewhat frequently, "
            "so just try again in a minute or so."
        )
        exit(2)
        return

    # Check that the given directories are in the extracted spec folder
    if not directories:
        directories = DEFAULT_DIRS_TO_GENERATE
    for d in directories:
        dir_to_check = extracted_folder / d
        if not (dir_to_check.exists() and dir_to_check.is_dir()):
            raise NotADirectoryError(
                f'Unable to find directory "{d}" in extracted spec files. Check the '
                f"`directories` argument and try again."
            )

    # Clear the destination dir (minus a few things)
    rmrf(
        dst,
        exclude={
            Path("README.md"),
            Path("__init__.py"),
            Path("abstract_base.py"),
            Path("factory.py"),
            Path("field_types.py"),
            Path("tests"),
        },
    )
    dst.mkdir(exist_ok=True)
    (dst / "__init__.py").touch()

    # Copy all files from the templates folder except Jinja2 files
    for f in TEMPLATE_DIR.glob("**/*.[!jinja2]*"):
        dst_path = dst / f.relative_to(TEMPLATE_DIR)
        try:
            copy(f, dst_path)
        except FileNotFoundError:
            # Parent dir may not exist. Create it and then try the copy again.
            dst_path.parent.mkdir()
            copy(f, dst_path)

    process_files(extracted_folder, dst, directories, TEMPLATE_DIR)
    format_python_files(dst)


if __name__ == "__main__":
    main()
