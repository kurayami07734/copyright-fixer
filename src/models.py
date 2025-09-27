from dataclasses import dataclass
from datetime import date
from enum import StrEnum, auto
from typing import List, Optional


class CopyrightStatus(StrEnum):
    """Defines the possible states of a copyright notice."""

    OK = auto()
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
class Line:
    """Represents a single line in a source file."""

    line_number: int
    content: str


@dataclass
class SourceFile:
    """Represents a single source file's identity and full content."""

    path: str
    lines: List[Line]


@dataclass
class AnalysisResult:
    """Provides a detailed report on the copyright status of one file."""

    file: SourceFile
    status: CopyrightStatus
    line_number: Optional[int] = None
