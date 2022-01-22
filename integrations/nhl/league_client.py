from integrations.nhl.base_client import NHLClient


class LeagueClient(NHLClient):
    def __init__(self):
        super().__init__()

    def get_conference(self, conference_id: int) -> dict:
        response = self._get('conferences', conference_id)
        return NHLClient.return_json_content(response, 'conferences')

    def get_team(self, team_id: int) -> dict:
        response = self._get('teams', team_id)
        return NHLClient.return_json_content(response, 'teams')

    def get_division(self, division_id: int) -> dict:
        return self._get('divisions', division_id).json().get('divisions')[0]

    def get_franchise(self, franchise_id: int) -> dict:
        return self._get('franchises', franchise_id).json().get('franchises')[0]

    def get_all_active_conferences(self) -> list:
        return self._get('conferences').json().get('conferences')

    def get_all_active_divisions(self) -> list:
        return self._get('divisions').json().get('divisions')

    def get_all_active_teams(self) -> list:
        return self._get('teams').json().get('teams')
