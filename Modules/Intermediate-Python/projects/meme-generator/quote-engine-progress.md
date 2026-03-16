# Quote Engine Progress Tracker

## Project Context

| Topic | Status | Notes |
|---|---|---|
| Module responsibility | Active | The Quote Engine module is responsible for ingesting many file types that contain quotes. A quote contains a `body` and an `author`. |
| Design goal | Active | This module should demonstrate understanding of complex inheritance, abstract classes, class methods, strategy objects, and other core programming principles. |
| Quote format | Active | Quotes are represented like: `"This is a quote body" - Author` |
| Source files | Active | Example quote files are in `./_data/SimpleLines` and `./_data/DogQuotes`. The goal is to extract quotes line by line from these files. |
| Interface contract | Active | `IngestorInterface` must define `can_ingest(cls, path: str) -> boolean` and `parse(cls, path: str) -> List[QuoteModel]`. |
| Strategy pattern | Active | Separate strategy/helper classes should implement the interface for `csv`, `docx`, `pdf`, and `txt`. |
| Final ingestor | Active | The final `Ingestor` class should use the interface and choose the correct parser based on file type. |
| PDF requirement | Active | PDF parsing should use Xpdf via the `subprocess` module. Do not use the PyPI `pdftotext` package for this project. |
| Environment note | Active | Xpdf may need to be installed locally and added to PATH, especially on Windows. |

## Functionality

| Task | Status | Notes |
|---|---|---|
| Create `QuoteEngine` package | Pending | Create a Python module, including `__init__.py`, inside a directory called `QuoteEngine`. |
| Review provided quote files | Pending | Example quotes are provided in a variety of files. Review the file formats in `./_data/SimpleLines` and `./_data/DogQuotes`. |
| Implement `QuoteModel` | Pending | Implement a simple `QuoteModel` class to encapsulate the quote `body` and `author`. |
| Implement `IngestorInterface` | Pending | Implement an abstract base class `IngestorInterface`. This class should define two class methods with the signatures `def can_ingest(cls, path) -> boolean` and `def parse(cls, path: str) -> List[QuoteModel]`. |
| Implement TXT ingestor | Pending | Implement a strategy object that realizes `IngestorInterface` for `.txt` files. |
| Implement CSV ingestor | Pending | Implement a strategy object that realizes `IngestorInterface` for `.csv` files. |
| Implement DOCX ingestor | Pending | Implement a strategy object that realizes `IngestorInterface` for `.docx` files. |
| Implement PDF ingestor | Pending | Implement a strategy object that realizes `IngestorInterface` for `.pdf` files using Xpdf and `subprocess`. |
| Implement final `Ingestor` | Pending | Implement a final `Ingestor` class that realizes the `IngestorInterface` abstract base class and encapsulates the helper classes. It should implement logic to select the appropriate helper for a given file, based on file type. |
| Check against rubric | Pending | If useful, compare the implementation against the Quote Engine Module section of the rubric. |

## Style

| Task | Status | Notes |
|---|---|---|
| Add clear docstrings | Pending | All Quote classes should have clear, concise, and PEP-compliant docstrings. |
| Check PEP 8 compliance | Pending | All code should be PEP 8 compliant. |
| Handle common exceptions | Pending | Common exceptions should be handled using try-catch blocks. |
| Remove starter comments | Pending | No `TODO` markers should remain in submitted code. |

## Validation

| Check | Status | Notes |
|---|---|---|
| TXT parser works | Pending | Confirm the TXT ingestor returns a `List[QuoteModel]` from a supported text file. |
| CSV parser works | Pending | Confirm the CSV ingestor returns a `List[QuoteModel]` from a supported CSV file. |
| DOCX parser works | Pending | Confirm the DOCX ingestor returns a `List[QuoteModel]` from a supported DOCX file. |
| PDF parser works | Pending | Confirm the PDF ingestor returns a `List[QuoteModel]` from a supported PDF file. |
| Final `Ingestor.parse()` works | Pending | Confirm the final `Ingestor` chooses the correct helper for each supported file type and parses successfully. |
