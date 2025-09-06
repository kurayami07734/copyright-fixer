import argparse as agp
from dataclasses import dataclass
from typing import List, Optional, Protocol


class CopyrightFixerArgs(Protocol):
    """A protocol to annotate types in the args object."""

    filenames: List[str]
    company_name: str
    comment_symbol: str


@dataclass
class File:
    filename: str
    comment_lines: list[str]


@dataclass
class CheckResult:
    ok: bool
    filename: str
    fix: Optional[str]


def parse_args() -> CopyrightFixerArgs:
    parser = agp.ArgumentParser(
        prog="copyright_fixer",
        description="A command-line tool to fix copyright notices",
    )

    parser.add_argument(
        "filenames",
        metavar="files",
        type=str,
        nargs="+",
        help="A list of file names to be processed.",
    )

    parser.add_argument(
        "--company_name",
        "-n",
        type=str,
        help="Name of the company",
        action="store",
        required=True,
    )

    parser.add_argument(
        "--comment_symbol",
        "-s",
        type=str,
        help="Symbol which starts a comment line",
        action="store",
        required=True,
    )

    return parser.parse_args()


def read_files(args: CopyrightFixerArgs) -> list[File]:
    files = []

    for filename in args.filenames:
        file = File(filename=filename, comment_lines=[])
        comment_lines = []

        with open(filename, mode="r") as file:
            for line in file.readlines():
                if line.startswith(args.comment_symbol):
                    comment_lines.append(line)

        file.comment_lines = comment_lines

        files.append(file)

    return files


def check_files(file: list[File], args: CopyrightFixerArgs) -> list[CheckResult]:
    pass


def write_fixes(results: list[CheckResult], args: CopyrightFixerArgs):
    pass


def main():
    args = parse_args()

    files = read_files(args)

    results = check_files(files, args)

    write_fixes(results, args)


if __name__ == "__main__":
    main()
