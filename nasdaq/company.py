from enum import Enum

from .base import Base


class Frequency(Enum):
    ANNUAL = 1,
    QUARTERLY = 2,


class HoldingType(Enum):
    pass


class Company(Base):
    def __init__(self, ticker):
        super().__init__(ticker=ticker, prefix='company')

    def get_company_profile(self):
        return self.endpoint(endpoint='company-profile')

    def get_insider_trades(self, limit=10, insider_type="ALL", sort_column="lastDate", sort_order="DESC"):
        params = {'limit': limit,
                  'type': insider_type,
                  'sortColumn': sort_column,
                  'sortOrder': sort_order}
        return self.endpoint(endpoint='insider-trades', params=params)

    def get_financials(self, frequency: Frequency = Frequency.ANNUAL):
        return self.endpoint(endpoint='financials', params={'frequency': frequency.value})

    def get_earnings_surprise(self):
        return self.endpoint('earnings-surprise')

    def get_institutional_holdings(self, limit=15, holding_type='TOTAL', sort_column='marketValue', sort_order='DESC'):
        params = {
            'limit': limit,
            'type': holding_type,
            'sortColumn': sort_column,
            'marketValue': sort_order,
        }
        return self.endpoint('institutional-holdings',
                             params=params)
