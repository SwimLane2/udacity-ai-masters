"""Define the interface for quote file ingestors."""

from abc import ABC, abstractmethod
from typing import List

from .QuoteModel import QuoteModel


class IngestorInterface(ABC):
    """Define a common interface for all quote ingestors."""

    allowed_extensions = []

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        """Return whether this class can ingest the given file path."""
        ext = path.split('.')[-1]
        return ext in cls.allowed_extensions

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse a file and return a list of QuoteModel objects."""
        pass
