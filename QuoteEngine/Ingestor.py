"""A class to provide one single interface to load different kinds of files.
"""

from .QuoteModel import QuoteModel
from .IngestorInterface import IngestorInterface
from .TextIngestor import TextIngestor
from .DocxIngestor import DocxIngestor
from .CSVIngestor import CSVIngestor
from .PDFIngestor import PDFIngestor
from typing import List


class Ingestor(IngestorInterface):
    """Merging all the ingestors into one single interface."""

    all_ingestors = [TextIngestor, DocxIngestor, CSVIngestor, PDFIngestor]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse an input file."""
        for each_ingestor in cls.all_ingestors:
            if each_ingestor.can_ingest(path):
                return each_ingestor.parse(path)
