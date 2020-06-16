from flask import render_template
from web import blueprint_web as web
from api.v1.controllers.nhlApi import get_box_score


@web.route("/boxscore/<gameId>")
def boxscore(gameId):
    boxscore = get_box_score(gameId)
    print('boxscore',  boxscore)
    return render_template('boxscore.html', boxscore=boxscore)
