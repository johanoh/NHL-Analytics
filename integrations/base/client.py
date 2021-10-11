import requests
from requests import Response
from integrations.base.exceptions import ResponseError


class BaseClient:

    def __init__(self, host):
        self.host = host

    def _get(self, *args) -> Response:
        url = self.url_join(list(args))
        response = BaseClient.validate_response(requests.get(url))
        return response

    def url_join(self, args_list) -> str:
        args_list = list(map(str, args_list))
        return f'{self.host}/{"/".join(args_list)}'

    @classmethod
    def validate_response(cls, response):
        if response.status_code == 200:
            return response
        else:
            raise ResponseError(f'invalid response: {response.status_code}')
