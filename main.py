from flask import Flask,jsonify,request
import csv

all_articles = []
file = open('articles.csv')
reader = csv.reader(file)

data = list(reader)
all_articles = data[1:]

liked_articles = []
disliked_articles = []
unwatched = []

app = Flask(__name__)
@app.route('/get-article')

def get_articles():
    return jsonify({
        'data':all_articles[0],
        'status':'success'
    })

@app.route('/liked-article',methods = ['POST'])

def liked_article():
    article = all_articles[0]
    all_articles = all_articles[1:]
    liked_articles.append(article)
    return jsonify({
        'status':'success'
    }),201

@app.route('/disliked-article',methods = ['POST'])

def disliked_article():
    article = all_articles[0]
    all_articles = all_articles[1:]
    disliked_articles.append(article)
    return jsonify({
        'status':'success'
    }),201