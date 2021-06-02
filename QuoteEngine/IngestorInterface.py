"""An abstract class to parse files."""

from .QuoteModel import QuoteModel
from abc import ABC, abstractmethod
from typing import List


class IngestorInterface(ABC):
    """Class for parsing files."""

    input_files_formats = []

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        """Determine a file extension and its correctness."""
        file_extension = path.split('.')[-1].lower()
        return file_extension in cls.input_files_formats

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse a file content."""
        pass
