# -*- coding: utf-8 -*-
from pathlib import Path
from zipfile import BadZipFile, ZipFile

import click
import requests
from requests import HTTPError

# noinspection PyPackageRequirements
from retry import retry

from .utils import rmrf


def download_and_extract(
    spec_url: str,
    working_dir: Path,
    force_download: bool = False,
) -> Path:
    """Download then extract the spec, return dir where extracted."""
    spec_path = Path(spec_url)
    spec_zip = working_dir / spec_path.name

    _download(spec_url, spec_zip, force_download)
    return _extract(spec_path, spec_zip)


@retry(HTTPError, tries=10, delay=2, backoff=1.5)
def _download(spec_url: str, spec_zip: Path, force_download: bool):

    # TODO: May need to update this logic to download a newer version of the spec
    if force_download or not spec_zip.exists():
        click.echo(f"Downloading Redox spec from {spec_url}...", nl=False)
        schemas = requests.get(
            spec_url,
            headers={
                "Accept-Encoding": "gzip, deflate, br",
                "User-Agent": "PostmanRuntime/7.29.0",
            },
        )
        try:
            schemas.raise_for_status()
        except HTTPError:
            click.echo(f"Error (HTTP {schemas.status_code})")
            raise

        with open(spec_zip, "wb") as fd:
            fd.write(schemas.content)

        click.echo("Done")
    else:
        click.echo(f"Found existing spec zip file at {spec_zip}\nSkipping download")


def _extract(spec_path: Path, spec_zip: Path) -> Path:
    # Create or clear extraction folder
    dst_dir = spec_zip.parent / spec_path.stem
    try:
        dst_dir.mkdir(exist_ok=False)
    except FileExistsError:
        rmrf(dst_dir)
        dst_dir.mkdir()
    (dst_dir / "__init__.py").touch()

    click.echo("Unzipping spec")
    try:
        with ZipFile(spec_zip, "r") as zippy:
            zippy.extractall(path=dst_dir)
    except BadZipFile:
        click.echo(
            "Unable to read zip file contents. There must have been an error "
            "when downloading. Sometimes the request will succeed if you try "
            "again in a few minutes."
        )
        raise

    return dst_dir
