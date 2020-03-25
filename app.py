from boggle import Boggle
from flask import Flask, render_template, request, session

app = Flask(__name__)
app.config['SECRET_KEY'] = "never-tell!"


boggle_game = Boggle()
board = boggle_game.make_board()

@app.route("/")
def home_board():
    """ Displays home board"""
    session['board'] = board

    print(session['board'])

    return render_template("home.html")
