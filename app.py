import os
from typing import List, Any

import easyocr

from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename

from ocr import *

app = Flask(__name__)

UPLOAD_FOLDER = 'static/uploads/'
IMAGE_PATH = UPLOAD_FOLDER + 'file'
app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        flash('No image selected for uploading')
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        flash('Image successfully uploaded and displayed below')
        return render_template('index.html', filename=filename)
    else:
        flash('Allowed image types are - png, jpg, jpeg, gif')
        return redirect(request.url)


@app.route('/display/<filename>')
def display_image(filename):
    output = check(show_result())
    # print('display_image filename: ' + filename)
    return redirect(url_for('static', filename='uploads/' + filename),data = output, code=301)


"""@app.route('/<output>')
def script_output():
    output = check(show_result())
    return render_template('Result.html', output=output)"""


"""@app.route('/', methods=['PAST'])
def show_result():
    reader = easyocr.Reader(['en'])
    result = reader.readtext('filename')
    a1 = []
    if len(result) == 0:
        flash('Given file is not invoice')
    else:
        for i in range(len(result)):
            x = result[i][1]
            a1.append(x)
        return a1


def check(a1):
    for i, word in zip(range(len(a1)), a1):
        if word in ["GSTIN", "GST/UIN", "GSTIN No"]:
            temp = a1[i + 1]
            return str(temp)"""

if __name__ == "__main__":
    app.run()
