"""A class to implement a user exception for file extensions."""


class InvalidFileExtension(Exception):
    """Implement exception for file extension."""

    def __init__(self, *args):
        """Initialize the class state."""
        self.default_message = 'The file is not in correct format'
        self.input_message = ''
        for value in args:
            self.input_message = value

    def __repr__(self):
        """Represent the class in a string format."""
        if len(self.input_message) != 0:
            return self.input_message
        else:
            return self.default_message
