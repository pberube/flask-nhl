# flask-nhl
Backend exploration with flask without database
## Prerequisites
* Python 3.7
* Flask  1.1.1
## Development
### Installation
    $ pip3 install -r requirements.txt
### Running
    $ python3 app.py run
### Unit Testing
    $ python3 app.py test
### Testing
    $ curl -X GET "http://127.0.0.1:32779/api/v1/nhl/games/boxscore/2018021155" -H "accept: application/json"
### Docker (build-start, stop)
    $ docker-compose -f "docker-compose.yml" up -d --build
    $ docker-compose -f "docker-compose.yml" down
## Endpoints  
|Endpoint|Method|Parameters|Description|
|:-|:-|:-|:-|
|/nhl/games/boxscore/{date}|GET|date of the game|Get the scoreboard of a game|
|/nhl/games/count|GET|none|Get the number of games today|
