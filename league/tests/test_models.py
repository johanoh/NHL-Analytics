import pytest

from ..models import (
    Conference,
    # Division,
    # Team,
    # Franchise
)


@pytest.mark.unit
@pytest.mark.django_db
def test_conference():

    # given
    conference_id = 1
    conference_name = 'Eastern'
    conference_link = '/api/v1/conferences/1'
    conference_short_name = 'XVE'
    conference_active = False

    # when
    conference_obj = Conference(
        id=conference_id,
        name=conference_name,
        link=conference_link,
        short_name=conference_short_name,
        active=conference_active
    )

    # then
    assert conference_id == conference_obj.id
    assert conference_name == conference_obj.name
    assert conference_link == conference_obj.link
    assert conference_active == conference_obj.active
