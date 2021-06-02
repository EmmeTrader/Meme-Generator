"""A class to ingest docx files using the native file library."""

from .QuoteModel import QuoteModel
from .IngestorInterface import IngestorInterface
from typing import List
from .InvalidFileExtension import InvalidFileExtension
from docx import Document


class DocxIngestor(IngestorInterface):
    """Class to parse docx files."""

    input_files_formats = ['docx']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse a docx file."""
        quote_objects = []

        try:
            is_file_exist = open(path)
            if cls.can_ingest(path):

                docx_to_read = Document(path)
                for each_row in docx_to_read.paragraphs:
                    if len(each_row.text) != 0:
                        body_text, author = each_row.text.split('-')
                        quote_objects.append(
                            QuoteModel(body_text.strip(), author.strip())
                        )
                    else:
                        pass
            else:
                raise InvalidFileExtension('The file extension is not docx')

        except FileNotFoundError:
            print('The file is not found')

        return quote_objects
