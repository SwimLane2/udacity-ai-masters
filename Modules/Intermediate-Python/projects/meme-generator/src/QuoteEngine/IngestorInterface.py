"""Define the interface for quote file ingestors."""

from abc import ABC, abstractmethod


class IngestorInterface(ABC):
    """Define a common interface for all quote ingestors."""

    allowed_extensions = []

    @classmethod
    def can_ingest(cls, path) -> boolean:
        """Return boolean value (TRUE/FALSE) whether the given file path can be ingested by this class."""
        ext = path.split('.')[-1]
        return ext in cls.allowed_extensions

    @classmethod
    @abstractmethod
    def parse(cls, path) -> list[QuoteModel]:
        """Parse a file and return a list of QuoteModel objects."""
        pass
