import requests
from django.conf import settings


def get_conference(conference_id):

    conference = requests.get(
        f'{settings.NHL_BASE_URL}/conferences/{conference_id}'
    )
    if conference.status_code != 200:
        return 'invalid conference ID'
    return conference.json().get('conferences')[0]

def get_division(division_id):

    division = requests.get(
        f'{settings.NHL_BASE_URL}/divisions/{division_id}'
    )
    if division.status_code !=  200:
        return 'invalid division id'
    return division.json().get('divisions')[0]

def get_team(team_id):

    team = requests.get(
        f'{settings.NHL_BASE_URL}/teams/{team_id}'
    )
    if team.status_code != 200:
        return 'invalid team id'
    return team.json().get('teams')[0]

def get_franchise(franchise_id):

    franchise = requests.get(
        f'{settings.NHL_BASE_URL}/franchises/{franchise_id}'
    )

    if team.status_code != 200:
        return 'invalid franchise id'
    return franchise.json.get('franchises')[0]