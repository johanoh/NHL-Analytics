from requests_handler.league import (
    get_conference,
    get_division,
    get_team,
    get_franchise
)
from datetime import datetime
from league.models import (
    Conference,
    Division,
    Team,
    Franchise
)

def insert_conference():

    for i in range(100):
        response = get_conference(i)
        if type(response) == dict:
            Conference(
                id=response.get('id'),
                name=response.get('name'),
                link=response.get('link'),
                abbreviation=response.get('abbreviation'),
                short_name=response.get('shortName'),
                active=response.get('active')
            ).save()

def insert_division():
    for i in range(100):
        response = get_division(i)
        if type(response) == dict
        Division(
            id=response.get('id'),
            name=response.get('name'),
            abbreviation=response.get('abbreviation'),
            active=response.get('active'),
            conference_id=response.get('conference').get('id')
        ).save()

def insert_team():
    for i in range(100):
        response=get_team()
        if type(response) == dict:
            franchise=get_franchise(response.get('franchise').get('id'))
            Franchise(
                id=franchise.get('franchiseId'),
                first_year_of_play=datetime.date(
                    franchise.get('firstSeasonId')[:4],
                    1,
                    1
                ),
                most_recent_team_id=r
            )
        