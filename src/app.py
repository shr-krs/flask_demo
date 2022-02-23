from flask import Flask, render_template, jsonify
import datetime
import random


app = Flask(__name__, static_folder="static")

@app.route("/")
def index():
    now = datetime.datetime.now()
    omikuji = ["大吉","吉","末吉","凶","大凶"]
    unsei = random.choice(omikuji)

    return render_template("index.html", now=now, unsei=unsei, omikuji=omikuji)


@app.route("/now")
def now():
    now = datetime.datetime.now()
    json = {"now":now}
    return jsonify(json)

@app.route("/clock")
def clock():
    return render_template("clock.html")