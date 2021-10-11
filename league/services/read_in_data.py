from datetime import datetime

from integrations.nhl.client import LeagueClient


from league.models import Conference, Division, Team, Franchise

client = LeagueClient()

def insert_conference(conference_id):

    response = client.get_conference(conference_id)
    if type(response) == dict:
        Conference(
            id=response.get('id'),
            name=response.get('name'),
            link=response.get('link'),
            abbreviation=response.get('abbreviation'),
            short_name=response.get('shortName'),
            active=response.get('active')
        ).save()


def insert_division(division_id):

    response = client.get_division(division_id)
    if type(response) == dict:
        conference_id = response.get('conference').get('id')
        if not check_unique_id(Conference, conference_id):
            insert_conference(conference_id)
        conference = Conference.objects.get(id=conference_id)
        Division(
            id=response.get('id'),
            name=response.get('name'),
            link=response.get('link'),
            abbreviation=response.get('abbreviation'),
            active=response.get('active'),
            conference_id=conference
        ).save()


def insert_franchise(franchise_id):
    response = client.get_franchise(franchise_id)
    franchise = Franchise(
        id=response.get('franchiseId'),
        first_year_of_play=datetime(
            int(str(response.get('firstSeasonId'))[:4]), 1, 1
        ),
        most_recent_team_id=response.get('mostRecentTeamId'),
        link=response.get('link')
    )
    if check_unique_id(Franchise, response.get('franchiseId')):
        franchise.update()
    else:
        franchise.save()


def insert_team(team_id):
    response = client.get_team(team_id)
    if type(response) == dict:
        conference_id = response.get('conference').get('id')
        division_id = response.get('division').get('id')
        franchise_id = response.get('franchise').get('franchiseId')
        if not check_unique_id(Franchise, franchise_id):
            insert_franchise(franchise_id)
        if not check_unique_id(Conference, conference_id):
            insert_conference(conference_id)
        if not check_unique_id(Division, division_id):
            insert_division(division_id)
        conference = Conference.objects.get(id=conference_id)
        division = Division.objects.get(id=division_id)
        franchise = Franchise.objects.get(id=franchise_id)
        Team(
            id=response.get('id'),
            name=response.get('name'),
            link=response.get('link'),
            abbreviation=response.get('abbreviation'),
            team_name=response.get('teamName'),
            location_name=response.get('locationName'),
            first_year_of_play=datetime(
                int(response.get('firstYearOfPlay')), 1, 1
            ),
            venue_name=response.get('venue').get('name'),
            venue_city=response.get('venue').get('city'),
            venue_tz_id=response.get('venue').get('timeZone').get('id'),
            venue_tz_offset=response.get('venue').get('timeZone').get('offset'),
            venue_tz_name=response.get('venue').get('timeZone').get('tz'),
            team_short_name=response.get('teamName'),
            active=response.get('active'),
            division_id=division,
            conference_id=conference,
            franchise_id=franchise,
        ).save()


def check_unique_id(league_object, value):
    if value in league_object.objects.all().values_list('id', flat=True):
        return True
    return False
