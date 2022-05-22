# -*- coding: utf-8 -*-
from pathlib import Path
from subprocess import CalledProcessError, run

import pytest
from snapshottest.file import FileSnapshot

import redox_lib_gen
from redox_lib_gen.utils import temp_chdir

from .no_spaces import NoSpacesPyTestSnapshotTest


def test_version():
    assert redox_lib_gen.__version__ == "0.1.0a1"


@pytest.fixture
def my_snapshot(request):
    with NoSpacesPyTestSnapshotTest(request) as snapshot_test:
        yield snapshot_test


@pytest.fixture
def fresh_lib_generation(tmp_path) -> Path:
    tmp_dir = Path(tmp_path).resolve() / "pyredox"
    tmp_dir.mkdir()

    # Change the working directory to be where generate.py file is
    with temp_chdir(Path(redox_lib_gen.__file__).parent):
        cmd = ["python3", "generate.py", "--dst", str(tmp_dir), "--force-download"]
        print(f"running command: `{' '.join(cmd)}`\n")
        try:
            call_result = run(cmd, check=True)
        except CalledProcessError as err:
            if err.returncode == 2:
                print(
                    "Generation of pyredox library failed due to issues downloading "
                    "the schema. It's possible the problem may be corrected when run "
                    "again, but for now there is no way to verify that any drift has "
                    "been accounted for in the library."
                )
            raise

    assert (
        call_result.returncode == 0
    ), f"Call to code generator failed with code {call_result.returncode}"
    return tmp_dir


def test_compare_generated_with_existing(my_snapshot, fresh_lib_generation: Path):
    tmp_dir = fresh_lib_generation
    for f in sorted(tmp_dir.glob("**/*.py")):
        my_snapshot.assert_match(FileSnapshot(str(f)))
