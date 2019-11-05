# views.py

from flask import render_template, request
import requests
import json
from app import app
import random

@app.route('/')
def index():
    r = requests.get("http://jservice.io/api/random?count=20")
    d = json.loads(r.text)
    # r = requests.get("http://jservice.io/api/random?count=20")
    # dB = json.loads(r.text)
    # dat = {key: value for (key, value) in (d.items() + dB.items())}
    return render_template("index.html", data=d)

@app.route('/', methods=['POST'])
def index_post():
    text = ""
    if 'value' in request.form:
        text = request.form['value']
        if (text == 'any'):
            r = requests.get("http://jservice.io/api/random?count=20")
        else:
            if 'startDate' in request.form:
                print(request.form['startDate'])
            r = requests.get("http://jservice.io/api/clues?value=" + text)
        d = json.loads(r.text)
    else :
        r = requests.get("http://jservice.io/api/random?count=20")
        d = json.loads(r.text)
    return render_template('index.html', data=d, text=text)

@app.route('/categories')
def categories():
    offset = random.randrange(0, 11510, 1)
    r = requests.get("http://jservice.io/api/categories?count=20&offset="+str(offset))
    d = json.loads(r.text)
    return render_template('categories.html', data=d, offset=offset)

@app.route('/categories', methods=['POST'])
def categories_post():
    offset = int(request.form['next'])
    print(offset)
    offset += 20
    r = requests.get("http://jservice.io/api/categories?count=20&offset="+str(offset))
    d = json.loads(r.text)
    return render_template('categories.html', data=d, offset=offset)

@app.route('/categoryclues/<id>')
def category_by_id(id):
    r = requests.get("http://jservice.io/api/clues?category="+str(id))
    d = json.loads(r.text)
    name = d[0]['category']['title'].title()
    return render_template('categoryclues.html', data=d, name=name)

# @app.route('/about')
# def about():
#     return render_template("about.html")