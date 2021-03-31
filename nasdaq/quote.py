from datetime import datetime, timedelta

from nasdaq.base import Base


class Quote(Base):
    def __init__(self, ticker, assetclass):
        super().__init__(ticker=ticker, prefix='quote')
        self._assetclass = assetclass

    def get_info(self):
        return self.endpoint(endpoint='info', params={'assetclass': self._assetclass})

    def get_realtime_trades(self, limit: int = 5):
        return self.endpoint(endpoint='realtime-trades', params={'limit': limit})

    def get_pre_market(self):
        params = {'markettype': 'pre', 'assetclass': self._assetclass}
        return self.endpoint(endpoint='extended-trading', params=params)

    def get_after_hours(self):
        params = {'markettype': 'post', 'assetclass': self._assetclass}
        return self.endpoint(endpoint='extended-trading', params=params)


    def get_dividends(self):
        return self.endpoint(endpoint='dividends', params={'assetclass': self._assetclass})

    def get_history(self, fromdate: datetime = datetime.today(),
                    todate: datetime = datetime.today() - timedelta(days=365)):
        params = {'assetclass': self._assetclass,
                  'fromdate': fromdate.date().strftime('%Y-%m-%d'),
                  'todate': todate.date().strftime('%Y-%m-%d'),
                  'limit': (todate - fromdate).days
                  }
        return self.endpoint(endpoint='historical', params=params)

    def get_eps(self):
        return self.endpoint(endpoint='eps')
