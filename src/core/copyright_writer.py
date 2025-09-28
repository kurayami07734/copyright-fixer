from datetime import date
from src.models import AnalysisResult, AppConfig, CopyrightStatus


class CopyrightWriter:
    """Writes fixes to files on disk based on analysis results."""

    def __init__(self, config: AppConfig):
        """Initializes the writer with the application configuration."""
        self._config = config

    def fix(self, result: AnalysisResult) -> bool:
        """
        Modifies a file on disk if the analysis found it to be outdated or missing.

        Args:
            result: The AnalysisResult for a given file.

        Returns:
            True if the file was modified, False otherwise.
        """
        if result.status == CopyrightStatus.OK:
            return False

        current_year = date.today().year
        new_line = f"{self._config.comment_symbol} Copyright (c) {current_year} {self._config.company_name}\n"

        with open(result.file.path, "r+") as f:
            lines = f.readlines()

            if result.status == CopyrightStatus.MISSING:
                lines.insert(0, new_line)
            elif result.status == CopyrightStatus.OUTDATED and result.line_number:
                line_index = result.line_number - 1
                original_line = lines[line_index]
                year_part = original_line.split("Copyright (c) ")[1].split(" ")[0]

                if "-" in year_part:
                    start_year, _ = year_part.split("-")
                    new_line = f"{self._config.comment_symbol} Copyright (c) {start_year}-{current_year} {self._config.company_name}\n"
                else:
                    start_year = year_part
                    new_line = f"{self._config.comment_symbol} Copyright (c) {start_year}-{current_year} {self._config.company_name}\n"

                lines[line_index] = new_line

            f.seek(0)
            f.writelines(lines)

        return True
