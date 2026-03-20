"""Ingest quotes from CSV files."""

import pandas as pd

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
            dataframe = pd.read_csv(path)
            for _, row in dataframe.iterrows():
                body = row['body']
                author = row['author']
                quotes.append(QuoteModel(body, author))

        except (FileNotFoundError, ValueError, KeyError) as e:
            raise ValueError(f'Error while parsing CSV file: {e}') from e

        return quotes
