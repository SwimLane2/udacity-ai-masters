"""Ingest quotes from plain text files."""

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class TXTIngestor(IngestorInterface):
    """Read quotes from TXT files."""

    allowed_extensions = ['txt']

    @classmethod
    def parse(cls, path):
        """Parse a TXT file and return a list of QuoteModel objects."""
        if not cls.can_ingest(path):
            raise ValueError('Cannot ingest exception')

        quotes = []

        try:
            with open(path, 'r', encoding='utf-8') as infile:
                for line in infile.readlines():
                    line = line.strip()

                    if not line:
                        continue

                    body, author = line.rsplit(' - ', 1)
                    quotes.append(QuoteModel(body, author))

        except (FileNotFoundError, ValueError) as e:
            raise ValueError(f'Error while parsing ... file: {e}') from e

        return quotes
