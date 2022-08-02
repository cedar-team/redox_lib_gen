#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from datetime import date
from subprocess import CalledProcessError, run

import click

from redox_lib_gen.generate import LIB_DEST_DIR
from redox_lib_gen.utils import temp_chdir


def get_num_differences() -> int:
    with temp_chdir(LIB_DEST_DIR):
        # Git status, short format, which shows one change per line
        proc = run(
            ["git", "status", "--short"], capture_output=True, text=True, check=True
        )

    if proc.stdout.strip() == "":
        click.echo("No changes found")
        return 0

    click.echo("Changes found")
    # Count the number of non-empty lines in the command's output
    return sum(1 if len(line) else 0 for line in proc.stdout.splitlines())


def update_version():
    with temp_chdir(LIB_DEST_DIR):
        # Increment patch version
        run(["poetry", "version", "patch"], check=True)

        # Set the version number in pyredox.__version__
        run(
            "echo "
            '"'
            "# -*- coding: utf-8 -*-\n"
            '__version__ = \\"`poetry version --short`\\"'
            '"'
            f" > {LIB_DEST_DIR / '__init__.py'}",
            shell=True,
            check=True,
        )

        # Set version number in test_pyredox_version.py
        run(
            "echo "
            '"'
            "# -*- coding: utf-8 -*-\n"
            "from pyredox import __version__\n"
            "\n"
            "\n"
            "def test_version():\n"
            '    assert __version__ == \\"`poetry version --short`\\"'
            '"'
            f" > {LIB_DEST_DIR / '..' / 'tests' / 'test_pyredox_version.py'}",
            shell=True,
            check=True,
        )


def add_commit_push(num_differences: int) -> str:
    """Create a git branch with the changes and push it."""
    today = date.today().isoformat()
    branch_name = f"lib_gen_{today}"
    msg = f"{today}: {num_differences} changes found"

    with temp_chdir(LIB_DEST_DIR):
        run(["git", "checkout", "-b", branch_name], check=True)
        run(["git", "add", "--all"], check=True)
        run(["git", "commit", "-m", msg], check=True)
        run(["git", "push", "--set-upstream", "origin", branch_name], check=True)

    click.echo(f"Changes pushed to origin on branch {branch_name}")
    return branch_name


def open_pr():
    # See https://hub.github.com/hub-pull-request.1.html for docs
    with temp_chdir(LIB_DEST_DIR):
        run(["hub", "pull-request", "--base", "main", "--no-edit"], check=True)


@click.command()
def main():
    try:
        if num_differences := get_num_differences():
            update_version()
            add_commit_push(num_differences)
            open_pr()
    except CalledProcessError as e:
        click.echo(f"Command failed: `{e.cmd}`")
        return 1


if __name__ == "__main__":
    exit(main())
