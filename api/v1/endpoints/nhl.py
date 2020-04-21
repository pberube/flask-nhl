from flask import request
from flask_restplus import Namespace, Resource

from api.v1.controllers.nhlController import NhlController

api = Namespace('nhl', description="nhl today's game")

nhl_controller = NhlController()


@api.route('/games/count')
@api.doc(security='authorization_key')
@api.response(200, 'Success')
class GameCount(Resource):
    def get(self):
        kwargs = {}
        args = []
        for key, value in request.args.items():
            if value:
                kwargs.update({key: value})
            else:
                args.append(key)
        return nhl_controller.games_count(*args, **kwargs)


@api.route('/games/boxscore/<date>')
@api.doc(security='authorization_key')
@api.response(200, 'Success')
class GameBoxScore(Resource):
    def get(self, date):
        return nhl_controller.box_score(date)

