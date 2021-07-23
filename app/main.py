from flask import Flask, request, render_template
import sklearn
import pickle
import pandas as pd
import numpy as np
import os
from flask_cors import cross_origin
from utils import get_base_url, allowed_file, and_syntax
from spam_or_ham import predict
from classifier import predict_with_percent

# setup the webservver
# port = 1234
# base_url = get_base_url(port)
# app = Flask(__name__, static_url_path=base_url+'static')

app = Flask(__name__)

IMAGE_FOLDER=os.path.join('static','images')
app.config['UPLOAD_FOLDER']=IMAGE_FOLDER

# @app.route(base_url)
def home():
    return render_template('home.html')

@app.route("#", methods=["GET","POST"])
@cross_origin()
def result():
    if request.method=="POST":
        review = (request.form["Review"])
        prediction = predict(review)
#         _, certainty = predict_with_percent(review)
#         certainty = round(certainty, 3) 
        output=""
        if not "not" in prediction:
            output="spam!" # +  " certainty: " + str(certainty)
        else:
            output="not spam!" #+ " certainty: " + str(100 - certainty)
    return render_template('home.html',prediction_text=f' {output}')
    return render_template("home.html")

if __name__ == "__main__":
    # change the code.ai-camp.org to the site where you are editing this file.
    print("Try to open\n\n    https://cocalc3.ai-camp.org" + base_url + '\n\n')
    # remove debug=True when deploying it
    app.run(host = '0.0.0.0', port=port, debug=True)
    import sys; sys.exit(0)
