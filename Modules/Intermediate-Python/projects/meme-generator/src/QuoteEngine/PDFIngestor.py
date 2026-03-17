"""Ingest quotes from PDF files."""

import os
import re
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
                contents = infile.read().strip()

                matches = re.findall(r'"(.*?)"\s*-\s*([^"]+)', contents)

                for body, author in matches:
                    quotes.append(QuoteModel(body.strip(), author.strip()))

        except Exception as e:
            print(f'Error while parsing PDF file: {e}')

        finally:
            if os.path.exists(temp_file):
                os.remove(temp_file)

        return quotes
