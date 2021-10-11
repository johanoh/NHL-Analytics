import pytest

from django.conf import settings

from integrations.base.client import BaseClient

@pytest.mark.parametrize('args_list, expected_output', [
    (['1', 2], 'https://statsapi.web.nhl.com/api/v1/1/2'),
    (['1', '2'], 'https://statsapi.web.nhl.com/api/v1/1/2'),
])
@pytest.mark.unit
def test_url_join(args_list, expected_output):

    # given
    base_client = BaseClient(host=settings.NHL_BASE_URL)
    
    # when
    url = base_client.url_join(args_list)

    # then
    assert url == expected_output