from integrations.nhl.base_client import NHLClient

class PlayerClient(NHLClient):
    def __init__(self):
        super().__init__()

    def get_positions(self) -> list:
        return self._get('positions').json()

    def get_player(self, player_id) -> dict:
        response = self._get('people', player_id)
        return NHLClient.return_json_content(resposne, 'people')