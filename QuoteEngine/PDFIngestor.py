"""A class to ingest pdf files using the native file library."""

from .QuoteModel import QuoteModel
from .IngestorInterface import IngestorInterface
from typing import List
from .InvalidFileExtension import InvalidFileExtension
from subprocess import call


class PDFIngestor(IngestorInterface):
    """Class to parse pdf files."""

    input_files_formats = ['pdf']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse a pdf file."""
        quote_objects = []

        try:
            is_file_exist = open(path)
            if cls.can_ingest(path):

                txt_from_pdf = 'text.txt'
                pdf_load_to_txt = call([
                    'pdftotext', '-simple', path, txt_from_pdf
                ])

                with open(txt_from_pdf, 'r') as txt_file_to_read:
                    txt_file = txt_file_to_read.readlines()

                    for each_row in txt_file:
                        if each_row not in ('\n', '\x0c'):
                            body_text, author = each_row.split(' - ')
                            quote_objects.append(
                                QuoteModel(body_text.strip(), author.strip())
                            )
                        else:
                            pass
            else:
                raise InvalidFileExtension('The file extension is not pdf')

        except FileNotFoundError:
            print('The file is not found')

        return quote_objects
