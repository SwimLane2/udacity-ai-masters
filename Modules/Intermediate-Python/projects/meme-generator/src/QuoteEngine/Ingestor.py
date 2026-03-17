"""Select the correct ingestor for a given file type."""

from .IngestorInterface import IngestorInterface
from .TXTIngestor import TXTIngestor
from .CSVIngestor import CSVIngestor
from .DOCXIngestor import DOCXIngestor
from .PDFIngestor import PDFIngestor


class Ingestor(IngestorInterface):
    """Choose the appropriate ingestor based on file extension."""

    ingestors = [TXTIngestor, CSVIngestor, DOCXIngestor, PDFIngestor]

    @classmethod
    def parse(cls, path):
        """Parse a file using the first ingestor that supports it."""
        for ingestor in cls.ingestors:
            if ingestor.can_ingest(path):
                return ingestor.parse(path)

        raise ValueError('No available ingestor for this file type')
