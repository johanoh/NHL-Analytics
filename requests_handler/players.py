import requests
from django.conf import settings


class Player:



    @classmethod
    def get_player_overview(cls, player_id):
        player = requests.get(f'{settings.NHL_BASE_URL}/people/{player_id}')
        if player.status_code != 200:
            return 'invalid conference ID'
        return player.json().get('people')[0]

    # @classmethod
    # def get_player_single_season(cls, player_id, start_year, **kwargs):
    #     """
    #     **kwargs
    #     """
    #     player = 