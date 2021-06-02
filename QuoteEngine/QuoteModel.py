"""Defining QuoteModel objects.

This class defines a QuoteModel object,
which contains text fields for body and author.
"""


class QuoteModel:
    """The class that creates QuoteModel objects."""
    def __init__(self, body_text, author):
        """Class constructor."""
        self.body_text = body_text
        self.author = author

    def __repr__(self):
        """Representation for a QuoteModel object."""
        return f'{self.body_text} - {self.author}'
