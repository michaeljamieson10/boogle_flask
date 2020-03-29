from unittest import TestCase
from app import app
from flask import session
from boggle import Boggle
import json


class FlaskTests(TestCase):

    # TODO -- write tests for every view function / feature!
    def test_home_board(self):
        with app.test_client() as client:
            res = client.get('/')
            html = res.get_data(as_text=True)
            
            self.assertEqual(res.status_code, 200)
            self.assertIn('<div>Highest Score:  </div>', html)
    def test_guess(self):
        with app.test_client() as client:
            res = client.post('/guess',data=json.dumps(dict(userGuess='ten')),content_type='application/json')
            html = res.get_data(as_text=True)
            self.assertEqual(res.status_code, 200)
    def test_score(self):
        with app.test_client() as client:
            res = client.post('/score',data=json.dumps(dict(userScore=0)),content_type='application/json')
            html = res.get_data(as_text=True)
            self.assertEqual(res.status_code, 200)
