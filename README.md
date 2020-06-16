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
|/|GET|none|Get home page|
|/swagger|GET|none|Get the swagger page of the api|
|/nhl/games/count|GET|none|Get the number of games today|
|/nhl/games/boxscore/{gameId}|GET|date of the game|Get the scoreboard of a game|
|/nhl/games/away/scorers/{gameId}|GET|List of scorers for the away team|
|/nhl/games/home/scorers/{gameId}|GET|List of scorers for the home team|

## Day 1
* put file structure in place for restful api
* create first unit tests for parsing nhl endpoint response
* enable swagger
* create endpoint `/games/count`
* create endpoint `/games/boxscore/<date>`
* create endpoint `/games/home/scorers/<date>`
* create endpoint `/games/away/scorers/<date>`
* test endpoints with swagger
* create dockerfile and docker-compose file
* test docker image using swagger
## Day 2
* add file structure in place for web
* add a second blueprint for handling a web page
* redirect `/` to a hello world web page
* redirect `/swagger` to the swagger page as `/api/v1`
## Day 3
* trying to add a page with the boxscore of a game