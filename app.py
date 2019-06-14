#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import *

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'

alphabet = "abcdefghijklmnopqrstuvwxyz"

@app.route('/', methods=["GET", "POST"])
def index():
	return render_template('index.html')

@app.route('/encrypted', methods=["GET", "POST"])
def encrypted():
    if request.method == 'POST':
        text = request.form['text']
        delta = int(request.form['delta'])
        encrypted_text = ""
        for c in list(text.lower()):
            if c == " ":
                encrypted_text += " "
            for i, l in enumerate(alphabet):
                if c == l:
                    encrypted_text += alphabet[(i+delta)%26]
        return render_template('encrypted.html', text=text, delta=delta, encrypted_text=encrypted_text)


if __name__ == "__main__":
	app.run(debug=True, host='0.0.0.0', port=8888, threaded=True)
