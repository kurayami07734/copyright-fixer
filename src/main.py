from src.core.cli_parser import CliParser
from src.core.copyright_analyzer import CopyrightAnalyzer
from src.core.copyright_writer import CopyrightWriter
from src.core.file_reader import FileReader


def main():
    """The main entry point for the command-line tool."""

    parser = CliParser()
    config = parser.parse_args()

    reader = FileReader(config)
    source_files = reader.read_all()

    analyzer = CopyrightAnalyzer(config)
    writer = CopyrightWriter(config)

    for file in source_files:
        result = analyzer.analyze(file)
        was_fixed = writer.fix(result)

        if was_fixed:
            print(f"FIXED: {file.path} ({result.status.name})")
        else:
            print(f"OK: {file.path} ({result.status.name})")


if __name__ == "__main__":
    main()
