# Meme Generator

This project creates meme images by combining dog pictures with quotes.  
It includes both a command-line tool and a small Flask web application.

---

## Project Overview

The project has three main parts:

- `QuoteEngine` loads quotes from different file types  
- `MemeEngine` creates meme images by adding text to pictures  
- `meme.py` and `app.py` allow the user to run the project from the command line or in the browser  

---

## Features

- Read quotes from TXT, CSV, DOCX, and PDF files  
- Create meme images with quote text and author  
- Generate a random meme from the command line  
- Generate random memes in a Flask web app  
- Create a custom meme from an image URL in the web app  

---

## Project Modules

### QuoteEngine

This module is used to load and parse quotes.

It includes:

- `QuoteModel` to store the quote body and author  
- `IngestorInterface` as the base class for all ingestors  
- `TXTIngestor`, `CSVIngestor`, `DOCXIngestor`, and `PDFIngestor` for each file type  
- `Ingestor` to choose the correct ingestor automatically  

---

### MemeEngine

This module is used to create meme images.

It:
- opens an image  
- resizes it  
- adds the quote body and author  
- saves the new image  
- returns the output path  

---

### meme.py

This is the command-line script. It allows the user to generate a meme using optional arguments for image path, quote body, and author.

---

### app.py

This is the Flask web app. It can generate a random meme or create a custom meme from a user-submitted image URL.

---

## Dependencies

This project uses the following Python packages:

- Flask  
- requests  
- Pillow  
- python-docx  

It also requires Xpdf for PDF parsing using the `pdftotext` command.

---

## Setup

1. Open a terminal in the project root folder  
2. Create a virtual environment:

```bash
python -m venv .venv
```

3. Install the required packages:

```bash
python -m pip install -r requirements.txt
```

4. Make sure Xpdf is installed and that `pdftotext` works in your terminal  

---

## How to Run

### Run the CLI

From the project root, run:

```bash
python src/meme.py
```

Optional arguments:

- `--path` for a custom image path  
- `--body` for a custom quote body  
- `--author` for a custom quote author  

Example:

```bash
python src/meme.py --path "src/_data/photos/dog/xander_1.jpg" --body "Learning one step at a time" --author "Me"
```

---

### Run the Flask App

From the project root, run:

```bash
python src/app.py
```

Then open these URLs in your browser:

- http://127.0.0.1:5000/ for a random meme  
- http://127.0.0.1:5000/create for a custom meme  

---

## Example Usage

Random meme from CLI:

```bash
python src/meme.py
```

Custom quote from CLI:

```bash
python src/meme.py --body "Learning one step at a time" --author "Me"
```

Full custom meme from CLI:

```bash
python src/meme.py --path "src/_data/photos/dog/xander_1.jpg" --body "Learning one step at a time" --author "Me"
```

Web app:

- Open `/` to generate a random meme  
- Open `/create` to create your own meme  

---

## Notes

- PDF parsing depends on Xpdf and the `pdftotext` command  
- Generated meme images are saved in the `static` folder  
- Temporary downloaded images may be stored in the `tmp` folder during custom meme creation  
