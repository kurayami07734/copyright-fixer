from dataclasses import dataclass
from datetime import date
from enum import StrEnum, auto
from typing import List, Optional


class CopyrightStatus(StrEnum):
    """Defines the possible states of a copyright notice."""

    UP_TO_DATE = auto()
    OUTDATED = auto()
    MISSING = auto()


@dataclass
class AppConfig:
    """A data class to hold all runtime configurations."""

    filenames: List[str]
    company_name: str
    comment_symbol: str
    current_year: int = date.today().year


@dataclass
class SourceFile:
    """Represents a single source file's identity and full content."""

    path: str
    lines: List[str]


@dataclass
class AnalysisResult:
    """Provides a detailed report on the copyright status of one file."""

    source_file: SourceFile
    status: CopyrightStatus
    line_index: Optional[int] = None
    existing_start_year: Optional[int] = None
