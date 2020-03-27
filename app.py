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
    session['count']= session.get('count', 0) + 1
   
    return render_template("home.html")

@app.route("/guess", methods=['POST'])
def guess():
    """This is the guess route which does not refresh the page, just takes the guess value of user and puts it into the server using session
        then returns using jsonify json
     """
    session['board'] = board
    word = request.json
    print(word['userGuess'], file=sys.stderr)
    resultStatus = boggle_game.check_valid_word(board, word['userGuess'])
    print(resultStatus, file=sys.stderr)
    # session['userGuessSet'] = set("cat") 
    # for val in session['userGuessSet']: 
    #     print(val) 

    final = {'result': resultStatus}
    

    return jsonify(final)

@app.route("/score", methods=['POST'])
def score():
    session['score'] = request.json
    score = request.json
    session['highestScore'] = session.get('highestScore', 0) 
    if session['highestScore'] < session['score']['userScore']:
        session['highestScore'] = session['score']['userScore']
        print(session['highestScore'],"HIGHEST SCORE",file=sys.stderr)
        finalHighestS = session['highestScore']
        final = {'result': finalHighestS}
        return jsonify(final)

    print(session['score']['userScore'],file=sys.stderr)
    # print(session['score'])
    finalHighestS = session['highestScore']
    final = {'result': finalHighestS}
    return jsonify(final)


