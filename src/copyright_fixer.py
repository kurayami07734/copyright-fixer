import argparse as agp
from dataclasses import dataclass
from datetime import date
from typing import List, Protocol
import re


class CopyrightFixerArgs(Protocol):
    """A protocol to annotate types in the args object."""

    filenames: List[str]
    company_name: str
    comment_symbol: str


@dataclass
class Line:
    line_number: int
    content: str


@dataclass
class File:
    filename: str
    comment_lines: list[Line]


@dataclass
class CheckResult:
    ok: bool
    filename: str
    line_number: int


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

        with open(filename, mode="r") as f:
            for idx, line in enumerate(f.readlines()):
                if line.startswith(args.comment_symbol):
                    comment_lines.append(Line(line_number=idx + 1, content=line))

        file.comment_lines = comment_lines

        files.append(file)

    return files


def check_files(files: list[File], args: CopyrightFixerArgs) -> list[CheckResult]:
    current_year = date.today().year
    escaped_company_name = re.escape(args.company_name)

    regex_pattern = rf"^\s*{re.escape(args.comment_symbol)}\s*copyright\s+\(c\)\s+(\d{{4}}(?:-\d{{4}})?)\s+{escaped_company_name}\s*$"

    results = []

    for file in files:
        result = CheckResult(filename=file.filename, line_number=1, ok=False)
        for line in file.comment_lines:
            match = re.match(regex_pattern, line.content.strip(), re.IGNORECASE)
            if match:
                year_part = match.group(1)
                if "-" in year_part:
                    start_year, end_year = map(int, year_part.split("-"))
                    if end_year == current_year:
                        result.ok = True
                else:
                    start_year = int(year_part)
                    if start_year == current_year:
                        result.ok = True
                break
        results.append(result)

    return results


def write_fixes(results: list[CheckResult], args: CopyrightFixerArgs):
    pass


def main():
    args = parse_args()

    files = read_files(args)

    results = check_files(files, args)

    write_fixes(results, args)


if __name__ == "__main__":
    main()
