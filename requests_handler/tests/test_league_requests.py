import pytest

from requests_handler.league import (
    get_conference,
    # get_division,
    # get_franchise,
    # get_team
)


@pytest.mark.django_db
def test_get_conference():

    conference = get_conference(1)

    assert conference.get('id') == 1
    assert conference.get('name') == 'Eastern'
    assert conference.get('link') == '/api/v1/conferences/1'
    assert conference.get('shortName') == 'East'
    assert conference.get('active') is False
    assert conference.get('abbreviation') == 'XVE'
