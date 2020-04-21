from flask_testing import TestCase

from app import app
from api.v1.controllers.nhlApi import how_many_games_today, get_box_score, pretty_box_score


class TestNhlApi(TestCase):
    def create_app(self):
        app.config.from_object('api.config.TestingConfig')
        return app

    def test_how_many_games_today(self):
        games = how_many_games_today()
        self.assertEqual(0, games)

    def test_get_box_score(self):
        box_score = get_box_score(2018021155)
        measured = pretty_box_score(box_score)
        expected = '3rd Final Buffalo Sabres 4 (27 shots, 16 hits) vs Montréal Canadiens 7 (44 shots, 30 hits)'
        self.assertEqual(expected, measured)
