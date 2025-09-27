import argparse as agp

from src.models import AppConfig


class CliParser:
    """Parses command-line arguments and creates an AppConfig object."""

    def parse_args(self) -> AppConfig:
        """
        Defines CLI arguments, parses them, and returns a populated AppConfig.
        """

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

        args = parser.parse_args()

        return AppConfig(
            filenames=args.filenames,
            company_name=args.company_name,
            comment_symbol=args.comment_symbol,
        )
