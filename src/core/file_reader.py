from src.models import AppConfig, SourceFile


class FileReader:
    """Reads file contents from disk into SourceFile objects."""

    def __init__(self, app_config: AppConfig):
        self.app_config = app_config

    def read_all(self) -> list[SourceFile]:
        """
        Reads a list of files from disk.

        Args:
            filenames: A list of file paths to read.

        Returns:
            A list of SourceFile objects.
        """
        files = []

        for filename in self.app_config.filenames:
            comment_lines = []

            with open(filename, mode="r") as f:
                for line in f.readlines():
                    if line.startswith(self.app_config.comment_symbol):
                        comment_lines.append(line)

            file = SourceFile(path=filename, lines=comment_lines)

            files.append(file)

        return files
