"""Select the correct ingestor for a given file type."""

from .IngestorInterface import IngestorInterface
from .TextIngestor import TextIngestor
from .CSVIngestor import CSVIngestor
from .DocxIngestor import DocxIngestor
from .PDFIngestor import PDFIngestor


class Ingestor(IngestorInterface):
    """Choose the appropriate ingestor based on file extension."""

    ingestors = [TextIngestor, CSVIngestor, DocxIngestor, PDFIngestor]

    @classmethod
    def parse(cls, path):
        """Parse a file using the first ingestor that supports it."""
        for ingestor in cls.ingestors:
            if ingestor.can_ingest(path):
                return ingestor.parse(path)

        raise ValueError('No available ingestor for this file type')
