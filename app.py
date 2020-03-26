from boggle import Boggle
from flask import Flask, render_template, request, session, jsonify
# import json
import sys

app = Flask(__name__)
app.config['SECRET_KEY'] = "never-tell!"


boggle_game = Boggle()
board = boggle_game.make_board()

@app.route("/", methods=['GET', 'POST'])
def home_board():
    """ Displays home board"""
    session['board'] = board
   
    return render_template("home.html")

@app.route("/guess", methods=['POST'])
def guess():
    session['board'] = board
    word = request.json
    print(word['userGuess'], file=sys.stderr)
    print("THIS IS THE GUESS ROUTE", file=sys.stderr)
    crat = boggle_game.check_valid_word(board, word['userGuess'])
    print(crat, file=sys.stderr)
    final = {'result': crat}
    

    return jsonify(final)



