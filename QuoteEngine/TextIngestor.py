"""A class to ingest txt files."""

from .QuoteModel import QuoteModel
from .IngestorInterface import IngestorInterface
from typing import List
from .InvalidFileExtension import InvalidFileExtension


class TextIngestor(IngestorInterface):
    """Class to parse txt files."""

    input_files_formats = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse a text file."""
        quote_objects = []

        try:
            is_file_exist = open(path)
            if cls.can_ingest(path):

                with open(path, 'r') as txt_file_to_read:
                    txt_file = txt_file_to_read.readlines()

                    for each_row in txt_file:
                        print(each_row)
                        if each_row not in ('\n', '\x0c'):
                            body_text, author = each_row.split(' - ')
                            quote_objects.append(
                                QuoteModel(body_text.strip(), author.strip())
                            )
                        else:
                            pass
            else:
                raise InvalidFileExtension('The file extension is not txt')

        except FileNotFoundError:
            print('The file is not found')

        return quote_objects
