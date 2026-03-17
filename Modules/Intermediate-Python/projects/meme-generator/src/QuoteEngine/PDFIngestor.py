"""Ingest quotes from PDF files."""

import os
import subprocess

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class PDFIngestor(IngestorInterface):
    """Read quotes from PDF files."""

    allowed_extensions = ['pdf']

    @classmethod
    def parse(cls, path):
        """Parse a PDF file and return a list of QuoteModel objects."""
        if not cls.can_ingest(path):
            raise ValueError('Cannot ingest exception')

        quotes = []
        temp_file = 'temp.txt'

        try:
            call = ['pdftotext', path, temp_file]
            subprocess.call(call)

            with open(temp_file, 'r', encoding='utf-8') as infile:
                for line in infile.readlines():
                    line = line.strip()

                    if not line:
                        continue

                    body, author = line.split(' - ')
                    quotes.append(QuoteModel(body, author))

        except Exception as e:
            print(f'Error while parsing PDF file: {e}')

        finally:
            if os.path.exists(temp_file):
                os.remove(temp_file)

        return quotes
