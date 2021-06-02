"""Flask application.

This app uses the Quote Engine and Meme Engine Modules
to generate a random captioned image.

It uses the requests package to fetch an image from a user submitted URL.
"""

import random
import os
import requests
from flask import Flask, render_template, request

from MemeEngine import MemeGenerator
from QuoteEngine import Ingestor, QuoteModel

app = Flask(__name__)
meme = MemeGenerator('./static')


def setup():
    """Loading all resources."""
    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv']

    quotes = []
    for each_file in quote_files:
        quotes.extend(Ingestor.parse(each_file))

    images_path = "./_data/photos/dog/"
    imgs = []
    for root, dirs, files in os.walk(images_path):
        imgs = [os.path.join(root, name) for name in files]

    return quotes, imgs


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """Generating a random meme."""
    img = random.choice(imgs)
    quote = random.choice(quotes)
    path = meme.make_meme(img, quote.body_text, quote.author)
    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """User input for meme information."""
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """Creating a user defined meme."""
    image_url = request.form['image_url']
    text_body = QuoteModel(request.form['body'], request.form['author'])
    response = requests.get(image_url)
    path_temp = './temp/image_temp.png'

    # write a temp image to a disk
    with open(path_temp, 'wb') as write_temp_image:
        write_temp_image.write(response.content)

    # meme generation
    path = meme.make_meme(path_temp, text_body.body_text, text_body.author)

    # remove the temp image
    os.remove(path_temp)

    return render_template('meme.html', path=path)


if __name__ == "__main__":
    app.run()
