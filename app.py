import pickle
from flask import flask, request, app, jsonify, url_for, render_template
import numpy as np
import pandas as pd

app = flask(__name__)
#loading the logistic regression model
regmodel = pickle.load(open('regmodel.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('home.html')
