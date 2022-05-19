# -*- coding: utf-8 -*-
from contextlib import contextmanager
from os import chdir, getcwd
from pathlib import Path


@contextmanager
def temp_chdir(path: str | Path):
    """Temporarily change the working directory."""
    previous_wd = getcwd()
    chdir(Path(path).resolve())
    try:
        yield
    finally:
        chdir(previous_wd)
