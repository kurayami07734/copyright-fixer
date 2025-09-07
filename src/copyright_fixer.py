import argparse as agp

from typing import List, Protocol


class ArgsProtocol(Protocol):
    """A protocol for the parsed command-line arguments."""

    filenames: List[str]
    company_name: str
    comment_symbol: str


def parse_args() -> ArgsProtocol:
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


def main():
    args = parse_args()
    print(args.filenames, args.comment_symbol, args.company_name)


if __name__ == "__main__":
    main()
