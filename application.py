#!/usr/bin/python
from flask import Flask, render_template, request
import time
import urllib.parse


application = Flask(__name__)
app = application
my_msg = "Wow this worked"


@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def home():

    if request.method == 'POST':
        return render_template("loading.html")
    return render_template("home.html")


@app.route('/loading')
def loading():
    return render_template("loading.html")


@app.route('/cat_subcat_list')
def cat_subcat_list():
    return render_template("success.html")


@app.route('/load_data')
def load_data():
    time.sleep(5)
    return "Map created"


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)