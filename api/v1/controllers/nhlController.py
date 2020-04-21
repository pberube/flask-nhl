from api.v1.controllers.nhlApi import how_many_games_today, get_box_score

class NhlController:
    def games_count(self, *args, **kwargs):
        return how_many_games_today(), 200

    def box_score(self, date):
        return get_box_score(date), 200
