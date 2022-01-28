import tempfile
from pathlib import Path
from typing import List

from behave.__main__ import main as behave_main
from behave.configuration import Configuration

__version__ = "0.1.0"


def run() -> bool:
    tmp = tempfile.NamedTemporaryFile()
    Configuration.defaults["show_timings"] = False
    path = Path.cwd().joinpath("features").as_posix()
    Configuration.defaults["dry_run"] = True
    behave_main([path, "--format", "steps.usage", "--outfile", tmp.name])

    with open(tmp.name) as openfile:
        lines = openfile.readlines()

    return find_unused_steps(lines)


def find_unused_steps(lines: List[str]) -> bool:
    result = []
    start_saving = False

    for line in lines:
        if line.startswith("UNUSED STEP DEFINITIONS"):
            start_saving = True
        if start_saving:
            result.append(line)

    print(result)
    return bool(result)
