import requests


def get(urn):
    r = requests.get(urn)
    r.raise_for_status()
    return r


def how_many_games_today():
    u = 'https://statsapi.web.nhl.com/api/v1/schedule'
    r = get(u)
    today_s_game = r.json()
    nb_games = 0
    if len(today_s_game['dates']):
        nb_games = len(today_s_game['dates'][0]['games'])
        print('# of games today', nb_games)
    return nb_games


def who_is_playing():
    u = 'https://statsapi.web.nhl.com/api/v1/schedule'
    r = get(u)
    today_s_game = r.json()
    print(today_s_game)
    print('# of games today', len(today_s_game['dates'][0]['games']))
    games = list()
    for game in today_s_game['dates'][0]['games']:
        game_id = game['gamePk']
        away = game['teams']['away']['team']['name']
        away_score = game['teams']['away']['score']
        home = game['teams']['home']['team']['name']
        home_score = game['teams']['home']['score']
        game_state = game['status']['abstractGameState']
        game_detailed_state = game['status']['detailedState']
        venue = game['venue']['name']
        games.append({'id': game_id, 'away': away, 'away_score': away_score, 'home': home, 'home_score': home_score, 'venue': venue,'state':game_state, 'detailed_state': game_detailed_state})
    return games


def print_games(games):
    for game in games:
        s = '{0} {1} {2} {3} {4} ({5}) {6} {7}'.format(game['id'], game['away'], game['away_score'], game['home'], game['home_score'], game['venue'], game['state'], game['detailed_state'])
        print(s)

def parse_box_score(game_feed):
    live_data = dict()
    live_data['period'] = game_feed['liveData']['linescore']['currentPeriodOrdinal']
    live_data['remaining'] = game_feed['liveData']['linescore']['currentPeriodTimeRemaining']
    live_data['home'] = dict()
    live_data['away'] = dict()
    live_data['home']['team'] = game_feed['liveData']['boxscore']['teams']['home']['team']['name']
    live_data['home']['goals'] = game_feed['liveData']['boxscore']['teams']['home']['teamStats']['teamSkaterStats']['goals']
    live_data['home']['shot_on_goal'] = game_feed['liveData']['boxscore']['teams']['home']['teamStats']['teamSkaterStats']['shots']
    live_data['home']['hits'] = game_feed['liveData']['boxscore']['teams']['home']['teamStats']['teamSkaterStats']['hits']
    live_data['home']['power_play'] = game_feed['liveData']['linescore']['teams']['home']['powerPlay']
    live_data['away']['team'] = game_feed['liveData']['boxscore']['teams']['away']['team']['name']
    live_data['away']['goals'] = game_feed['liveData']['boxscore']['teams']['away']['teamStats']['teamSkaterStats']['goals']
    live_data['away']['shot_on_goal'] = game_feed['liveData']['boxscore']['teams']['away']['teamStats']['teamSkaterStats']['shots']
    live_data['away']['hits'] = game_feed['liveData']['boxscore']['teams']['away']['teamStats']['teamSkaterStats']['hits']
    live_data['away']['power_play'] = game_feed['liveData']['linescore']['teams']['away']['powerPlay']
    return live_data


def pretty_box_score(g):
    away_info = '{0} {1} ({2} shots, {3} hits)'.format(g['away']['team'], g['away']['goals'], g['away']['shot_on_goal'], g['away']['hits'])
    home_info = '{0} {1} ({2} shots, {3} hits)'.format(g['home']['team'], g['home']['goals'], g['home']['shot_on_goal'], g['home']['hits'])
    return '{0} {1} {2} vs {3}'.format(g['period'], g['remaining'], away_info, home_info)


def get_box_score(game_id):
    u = 'https://statsapi.web.nhl.com/api/v1/game/{0}/feed/live'.format(game_id)
    r = get(u)
    game_feed = r.json()
    current_data = parse_box_score(game_feed)
    return current_data


def who_score(date, team):
    scorers = list()
    u = 'https://statsapi.web.nhl.com/api/v1/game/{0}/feed/live'.format(date)
    r = get(u)
    game_feed = r.json()
    players =  game_feed['liveData']['boxscore']['teams'][team]['players']
    for p in players:
        name = players[p]['person']['fullName']
        if players[p]['stats'] and len(players[p]['stats']) != 0:
            if 'skaterStats' in players[p]['stats'].keys():
                stats = players[p]['stats']['skaterStats']
                if stats['goals'] > 0 or stats['assists'] > 0:
                    scorers.append({name: {'goals': stats['goals'], 'assists': stats['assists']}})
    return scorers

