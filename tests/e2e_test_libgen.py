# -*- coding: utf-8 -*-
import os
from pathlib import Path
from subprocess import CalledProcessError, run
from tempfile import TemporaryDirectory
from typing import Optional
from warnings import warn

from snapshottest.file import FileSnapshot

from .file import FileTestCase


def fresh_lib_generation(tmp_path) -> Optional[Path]:
    tmp_dir = Path(tmp_path).resolve() / "pyredox"
    tmp_dir.mkdir()

    # Change the working directory to be where generate.py file is
    previous_wd = os.getcwd()
    os.chdir(Path(__file__).parent.parent)

    cmd = ["python3", "generate.py", "--dst", str(tmp_dir)]
    print(f"running command: `{' '.join(cmd)}`\n")
    try:
        call_result = run(cmd, check=True)
    except CalledProcessError as err:
        if err.returncode == 2:
            msg = (
                "Generation of pyredox library failed due to issues downloading the "
                "schema. It's possible the problem may be corrected when run again, "
                "but for now there is no way to verify that any drift has been "
                "accounted for in the library."
            )
            warn(msg)
            return

        print(f"Redox library generator exited with an error:\n{err}")
        raise

    # Re-set the current working directory to what it was before
    os.chdir(previous_wd)

    assert (
        call_result.returncode == 0
    ), f"Call to code generator failed with code {call_result.returncode}"
    return tmp_dir


class TestLibGen(FileTestCase):
    def test_compare_generated_with_existing(self):
        with TemporaryDirectory() as tmp_dir:
            lib_dir: Path = fresh_lib_generation(tmp_dir)

            if lib_dir is None:
                # Download failed
                return

            for f in sorted(lib_dir.glob("**/*.py")):
                self.assert_match_snapshot(FileSnapshot(str(f)))
