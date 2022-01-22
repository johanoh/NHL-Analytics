from integrations.base.client import BaseClient
from django.conf import settings


class NHLClient(BaseClient):

    def __init__(self, host=settings.NHL_BASE_URL):
        super().__init__(host=host)

    @staticmethod
    def return_json_content(response, main_key):
        return response.json().get(main_key)[0]
