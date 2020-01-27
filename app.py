import json
import urllib.request

from flask import Flask
from flask import request
#from fastai.vision import *

app = Flask(__name__)

@app.route('/predict')
def index():
    return json.dumps({"predictions": "dfjhk" });
