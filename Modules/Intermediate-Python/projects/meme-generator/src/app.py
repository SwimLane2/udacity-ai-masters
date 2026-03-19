"""Run the Flask web app for generating memes."""

import random
import os
import requests
from flask import Flask, render_template, abort, request

from QuoteEngine import Ingestor
from MemeEngine import MemeEngine

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__)

meme = MemeEngine(os.path.join(ROOT_DIR, 'static'))


def setup():
    """Load all resources."""
    quote_files = [
        os.path.join(ROOT_DIR, '_data', 'DogQuotes', 'DogQuotesTXT.txt'),
        os.path.join(ROOT_DIR, '_data', 'DogQuotes', 'DogQuotesDOCX.docx'),
        os.path.join(ROOT_DIR, '_data', 'DogQuotes', 'DogQuotesPDF.pdf'),
        os.path.join(ROOT_DIR, '_data', 'DogQuotes', 'DogQuotesCSV.csv'),
    ]

    quotes = []
    for file_path in quote_files:
        quotes.extend(Ingestor.parse(file_path))

    images_path = os.path.join(ROOT_DIR, '_data', 'photos', 'dog')

    imgs = []
    for root, _, files in os.walk(images_path):
        for file_name in files:
            imgs.append(os.path.join(root, file_name))

    return quotes, imgs


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """Generate a random meme."""
    img = random.choice(imgs)
    quote = random.choice(quotes)
    path = meme.make_meme(img, quote.body, quote.author)
    path = f'/static/{os.path.basename(path)}'

    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """Display the form for user meme input."""
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """Create a user defined meme."""
    image_url = request.form.get('image_url')
    body = request.form.get('body')
    author = request.form.get('author')

    temp_dir = os.path.join(ROOT_DIR, 'tmp')
    temp_path = os.path.join(temp_dir, 'temp_image.jpg')

    if not os.path.exists(temp_dir):
        os.makedirs(temp_dir)

    try:
        response = requests.get(image_url, timeout=10)

        with open(temp_path, 'wb') as outfile:
            outfile.write(response.content)

        path = meme.make_meme(temp_path, body, author)
        path = f'/static/{os.path.basename(path)}'

        os.remove(temp_path)

    except (requests.RequestException, IOError, ValueError):
        abort(500)

    return render_template('meme.html', path=path)


if __name__ == "__main__":
    app.run()
