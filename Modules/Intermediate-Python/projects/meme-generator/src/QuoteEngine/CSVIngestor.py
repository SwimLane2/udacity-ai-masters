"""Ingest quotes from CSV files."""

import csv

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class CSVIngestor(IngestorInterface):
    """Read quotes from CSV files."""

    allowed_extensions = ['csv']

    @classmethod
    def parse(cls, path):
        """Parse a CSV file and return a list of QuoteModel objects."""
        if not cls.can_ingest(path):
            raise ValueError('Cannot ingest exception')

        quotes = []

        try:
            with open(path, 'r', encoding='utf-8') as infile:
                reader = csv.DictReader(infile)
                for row in reader:
                    body = row['body']
                    author = row['author']
                    quotes.append(QuoteModel(body, author))

        except Exception as e:
            print(f'Error while parsing CSV file: {e}')

        return quotes
