from flask import *
from app import app
from flask import Flask, render_template, request
import sys

sys.path.append("/Users/2020shatgiskessell/Desktop/CS-Coding-Challenges-master/app/")
import model



@app.route('/')
@app.route('/index')
def results():
    return render_template('index.html')

@app.route('/results', methods=['GET', "POST"])
def shout():
    user_movies = []
    movie_options = ["The Incredibles", "Ratatouille", "Wreck-It Ralph", "Coraline","Tangled","Mulan","The Notebook","Mean Girls","The Proposal","She's the Man","Mis Congeniality","It", "Annabelle Comes Home", "Pyscho","The Ring","Gone Girl", "Murder on the Orient Express","The Da Vinci Code", "Arrival"]
    for movie in movie_options:
        if request.form.getlist(movie) == "on":
            user_movies.append(movie)
    output = model.movie_recomendor_2(user_movies)
    return render_template('results.html', output = output)
