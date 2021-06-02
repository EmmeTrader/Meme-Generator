"""A class to ingest csv files using the native file library."""

from .QuoteModel import QuoteModel
from .IngestorInterface import IngestorInterface
from typing import List
from .InvalidFileExtension import InvalidFileExtension
from csv import reader


class CSVIngestor(IngestorInterface):
    """Class to parse csv files."""

    input_files_formats = ['csv']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse a csv file."""
        quote_objects = []

        try:
            is_file_exist = open(path)
            if cls.can_ingest(path):

                with open(path, 'r') as csv_file_to_read:
                    csv_file = reader(csv_file_to_read)

                    for each_row in csv_file:
                        if len(each_row) != 0:
                            body_text, author = each_row[0], each_row[1]
                            quote_objects.append(
                                QuoteModel(body_text.strip(), author.strip())
                            )
                        else:
                            pass
            else:
                raise InvalidFileExtension('The file extension is not csv')

        except FileNotFoundError:
            print('The file is not found')

        return quote_objects
