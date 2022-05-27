import flask
from datetime import datetime
import pytz
import numpy as np
import pandas as pd
import math
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

app = flask.Flask(__name__)

def combine_features(data):
  features = []
  for i in range(0,data.shape[0]):
    features.append(data['Title'][i]+ ' '+ data['Authors'][i]+ ' '+data['Language'][i]+ ' '+data['Bookshelves'][i])
  return features

timezone = pytz.timezone("Asia/Kolkata")

def init():
    global cs
    df = pd.read_csv('out.csv', encoding='unicode_escape')
    columns =['Title', 'Authors', 'Language', 'Bookshelves']
    df['combined_features'] = combine_features(df)
    cm = CountVectorizer().fit_transform(df['combined_features'])
    cs = cosine_similarity(cm)


@app.route('/')
def homepage():
    the_time = datetime.now(timezone).strftime("%A, %d %b %Y %l:%M %p")
    return """
    <h1>Hello!</h1>
    <p>It is currently {time}.</p>
    <p>It is really easy to use this API.<br>
    Just make a GET request to the url/predict with id and size.<br>
    You'll get a json with the list of book predictions.</p>
    <p>BTW, Enjoy this picture of a cat.</p>
    <img src="http://loremflickr.com/600/400" />
    """.format(time=the_time)

@app.route("/predict", methods=["GET","POST"])
def predict():
    parameters = []
    parameters.append(flask.request.args.get('id'))
    parameters.append(flask.request.args.get('size'))
    if parameters[0] :
        scores = list(enumerate(cs[int(parameters[0])]))
        sorted_scores = sorted(scores, key= lambda x:x[1], reverse= True)
        if parameters[1] == None:
            parameters[1] = '10'
        sorted_scores = sorted_scores[0:int(parameters[1])]
        data = {"prediction": sorted_scores}
    else:
        data = {"error": "1"}
    return flask.jsonify(data)  

if __name__ == '__main__':
    init()
    app.run(debug=True, use_reloader=True)
