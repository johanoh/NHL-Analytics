from integrations.nhl.player_client import PlayerClient
from player.models import PrimaryPosition

client = PlayerClient()

def insert_player_positions():
    positions = client.get_positions()
    for position in positions:
        if not PrimaryPosition.objects.filter(position_code=position['code']):
            PrimaryPosition.objects.create(
                position_code = position['code'],
                position_name = position['fullName'],
                position_type = position['type'],
                position_abbrev = position['abbrev']
            )

def insert_player():
    player = client