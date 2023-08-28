# -*- coding: utf-8 -*-
from pathlib import Path
from subprocess import CalledProcessError, run

import pytest

import redox_parser_gen
from redox_parser_gen.utils import temp_chdir


def test_version():
    assert redox_parser_gen.__version__ == "0.1.0-alpha.1"


@pytest.fixture
def fresh_lib_generation(tmp_path) -> Path:
    tmp_dir = Path(tmp_path).resolve() / "redox_parser"
    tmp_dir.mkdir()

    # Change the working directory to be where generate.py file is
    with temp_chdir(Path(redox_parser_gen.__file__).parent):
        cmd = ["python3", "generate.py", "--dst", str(tmp_dir), "--force-download"]
        print(f"running command: `{' '.join(cmd)}`\n")
        try:
            call_result = run(cmd, check=True)
        except CalledProcessError as err:
            if err.returncode == 2:
                print(
                    "Generation of redox_parser library failed due to issues downloading "
                    "the schema. It's possible the problem may be corrected when run "
                    "again, but for now there is no way to verify that any drift has "
                    "been accounted for in the library."
                )
            raise

    assert (
        call_result.returncode == 0
    ), f"Call to code generator failed with code {call_result.returncode}"
    return tmp_dir


def test_compare_generated_with_existing(snapshot, fresh_lib_generation: Path):
    snapshot.snapshot_dir = Path(__file__).parent.resolve() / "snapshots"
    tmp_dir = fresh_lib_generation
    for f in tmp_dir.glob("**/*.py"):
        try:
            snapshot.assert_match(
                value=f.read_text(),
                snapshot_name=snapshot.snapshot_dir / f.relative_to(tmp_dir),
            )
        except AssertionError:
            print("Snapshot Mismatch... Do you need to run `pytest --snapshot-update`?")
            print(f"FAILED: {f}")
            raise
