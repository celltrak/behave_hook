import os
import sys
import tempfile
from glob import glob
from pathlib import Path
from typing import List

from behave.__main__ import main as behave_main


def run() -> bool:
    path_finder()
    execution_result = execute_behave()
    return find_unused_steps(execution_result)


def execute_behave() -> List[str]:
    tmp = tempfile.NamedTemporaryFile()
    behave_path = Path.cwd().joinpath("features").as_posix()
    behave_main(
        [
            behave_path,
            "--no-summary",
            "--format",
            "steps.usage",
            "--dry-run",
            "--outfile",
            tmp.name,
        ]
    )

    with open(tmp.name) as openfile:
        lines = openfile.readlines()

    return lines


def find_unused_steps(lines: List[str]) -> bool:
    exists_unused_steps = False

    for line in lines:
        if line.startswith("UNUSED STEP DEFINITIONS"):
            exists_unused_steps = True
        if exists_unused_steps:
            print(line)

    return exists_unused_steps


def path_finder() -> None:
    """Add app virtual env to Path"""
    paths = sys.path
    virtual_env = os.environ.get("PYENV_VIRTUAL_ENV")
    for venv_path in glob(f"{virtual_env}/lib/python*/site-packages"):
        if venv_path not in paths:
            paths.insert(0, venv_path)
    sys.path = paths
