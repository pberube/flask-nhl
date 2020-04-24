from flask_testing import TestCase

from app import app
from api.v1.controllers.nhlApi import how_many_games_today, get_box_score, pretty_box_score, who_score


class TestNhlApi(TestCase):
    def create_app(self):
        app.config.from_object('api.config.TestingConfig')
        return app

    def test_how_many_games_today(self):
        games = how_many_games_today()
        self.assertEqual(0, games)

    def test_get_box_score(self):
        expected = {"period": "3rd",
                    "remaining": "Final",
                    "home": {"team": "Montr\u00e9al Canadiens", "goals": 7, "shot_on_goal": 44, "hits": 30, "power_play": False},
                    "away": {"team": "Buffalo Sabres", "goals": 4, "shot_on_goal": 27, "hits": 16, "power_play": False}}
        box_score = get_box_score(2018021155)
        pretty = pretty_box_score(box_score)
        self.assertDictEqual(expected, box_score)
        self.assertEqual('3rd Final Buffalo Sabres 4 (27 shots, 16 hits) vs Montréal Canadiens 7 (44 shots, 30 hits)', pretty)

    def test_who_score(self):
        expected = [{'Matt Niskanen': {'goals': 0, 'assists': 1}},
                    {'Brooks Orpik': {'goals': 1, 'assists': 0}},
                    {'Alex Ovechkin': {'goals': 0, 'assists': 2}},
                    {'T.J. Oshie': {'goals': 1, 'assists': 1}},
                    {'Evgeny Kuznetsov': {'goals': 0, 'assists': 2}},
                    {'Dmitry Orlov': {'goals': 0, 'assists': 1}},
                    {'Nicklas Backstrom': {'goals': 1, 'assists': 1}},
                    {'Tom Wilson': {'goals': 1, 'assists': 0}}]
        scorers = who_score(2018030132, 'home')
        self.assertListEqual(expected, scorers)
