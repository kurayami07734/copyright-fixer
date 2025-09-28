from datetime import date
import re
from src.models import AnalysisResult, AppConfig, CopyrightStatus, SourceFile


class CopyrightAnalyzer:
    """Analyzes source files for copyright notice correctness."""

    def __init__(self, config: AppConfig):
        """
        Initializes the analyzer with the application configuration.

        This is where the regex pattern should be compiled.
        """
        self._config = config
        escaped_company_name = re.escape(self._config.company_name)
        self._pattern = re.compile(
            rf"^\s*{re.escape(self._config.comment_symbol)}\s*copyright\s+\(c\)\s+(\d{{4}}(?:-\d{{4}})?)\s+{escaped_company_name}\s*$",
            re.IGNORECASE,
        )

    def analyze(self, file: SourceFile) -> AnalysisResult:
        """
        Checks a single file for its copyright status.

        Args:
            file: The SourceFile object to analyze.

        Returns:
            An AnalysisResult object with the findings.
        """
        current_year = date.today().year
        result = AnalysisResult(
            file=file, status=CopyrightStatus.MISSING, line_number=None
        )

        for line in file.lines:
            match = self._pattern.match(line.content.strip())
            if match:
                year_part = match.group(1)
                if "-" in year_part:
                    _, end_year = map(int, year_part.split("-"))
                    if end_year == current_year:
                        result.status = CopyrightStatus.OK
                    else:
                        result.status = CopyrightStatus.OUTDATED
                else:
                    start_year = int(year_part)
                    if start_year == current_year:
                        result.status = CopyrightStatus.OK
                    else:
                        result.status = CopyrightStatus.OUTDATED

                result.line_number = line.line_number
                break

        return result
