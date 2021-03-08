import requests

headers = {'User-Agent': 'Chrome/89.0.4389.23'}


class Base:
    def __init__(self, ticker, prefix=None):
        self._ticker = ticker.upper()
        self._api_url = "https://api.nasdaq.com/api"
        self._prefix = prefix

    def _endpoint(self, endpoint, params=None):
        """
        :parameter
        :param endpoint API endpoint
        :param params Optional parameters for requests, entry limits, assetclass if needed, specify from-to datetime"""

        url = f'{self._api_url}/{self._prefix}/{self._ticker}/{endpoint}'
        return requests.get(url, headers=headers, params=params).json()['data']
