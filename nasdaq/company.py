from enum import Enum

from nasdaq.base import Base


class Frequency(Enum):
    ANNUAL = 1,
    QUARTERLY = 2,


class Company(Base):
    def __init__(self, ticker):
        super().__init__(ticker=ticker, prefix='company')

    def get_company_profile(self):
        return self._endpoint(endpoint='company-profile')

    def get_insider_trades(self, limit=10, insider_type="ALL", sort_column="lastDate", sort_order="DESC"):
        params = {'limit': limit,
                  'type': insider_type,
                  'sortColumn': sort_column,
                  'sortOrder': sort_order}
        return self._endpoint(endpoint='insider-trades', params=params)

    def get_financials(self, frequency: Frequency = Frequency.ANNUAL):
        return self._endpoint(endpoint='financials', params={'frequency': frequency.value})

    def get_earnings_surprise(self):
        return self._endpoint('earnings-surprise')