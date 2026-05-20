"""Ingest quotes from DOCX files."""

from docx import Document

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class DocxIngestor(IngestorInterface):
    """Read quotes from DOCX files."""

    allowed_extensions = ['docx']

    @classmethod
    def parse(cls, path):
        """Parse a DOCX file and return a list of QuoteModel objects."""
        if not cls.can_ingest(path):
            raise ValueError('Cannot ingest exception')

        quotes = []

        try:
            document = Document(path)

            for paragraph in document.paragraphs:
                line = paragraph.text.strip()

                if not line:
                    continue

                body, author = line.rsplit(' - ', 1)
                quotes.append(QuoteModel(body, author))

        except (FileNotFoundError, ValueError) as e:
            raise ValueError(f'Error while parsing ... file: {e}') from e

        return quotes
