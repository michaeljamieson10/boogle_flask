from boggle import Boggle
from flask import Flask, render_template, request, session, jsonify
import json
import sys

app = Flask(__name__)
app.config['SECRET_KEY'] = "never-tell!"


boggle_game = Boggle()
board = boggle_game.make_board()



@app.route("/", methods=['GET', 'POST'])
def home_board():
    """ Displays home board"""
    session['board'] = board
    session['count']= session.get('count', 0) + 1
    session["myList"] = []
    session["finalNum"] = 0


   
    return render_template("home.html")

@app.route("/guess", methods=['POST'])
def guess():
    """This is the guess route which does not refresh the page, just takes the guess value of user and puts it into the server using session
        then returns using jsonify json
     """
    session['board'] = board
    word = request.json
    print(word,"from json",file=sys.stderr)
    session["myList"] = session.get('myList', [])

    resultStatus = boggle_game.check_valid_word(board, word['userGuess'])
    if resultStatus == "ok":
        session["myList"].append(word['userGuess'])
    session["finalNum"] = 0

    my_set = set(session["myList"])
    for val in my_set: 
        session["finalNum"] += len(val)

    final = {
            'result': resultStatus,
            'finalNum' : session["finalNum"]
            }
    
    return jsonify(final)

@app.route("/score", methods=['POST'])
def score():
    """This is the score route, does not refresh page using ajax axios, 
        get the score sees if highest score is less thna current user score
        then returns"""
    session['score'] = request.json
    score = request.json
    print(session['score'],"from json",file=sys.stderr)
    session['highestScore'] = session.get('highestScore', 0) 
    if session['highestScore'] < session['score']['userScore']:
        session['highestScore'] = session['score']['userScore']
        finalHighestS = session['highestScore']
        final = {'result': finalHighestS}
        return jsonify(final)

    finalHighestS = session['highestScore']
    final = {'result': finalHighestS}
    return jsonify(final)
