"""Represent a quote with a body and an author."""


class QuoteModel:
    """Represent a quote with its body text and author."""

    def __init__(self, body, author):
        """Create a QuoteModel.

        :param body: The text of the quote.
        :param author: The author of the quote.
        """
        self.body = body
        self.author = author

    def __str__(self):
        """Return a human-readable string representation of the quote."""
        return f'"{self.body}" - {self.author}'
