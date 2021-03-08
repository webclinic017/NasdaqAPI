from nasdaq.base import Base


class Analyst(Base):
    def __init__(self, ticker):
        super().__init__(ticker=ticker, prefix='analyst')

    def get_estimate_momentum(self):
        return self._endpoint('estimate-momentum')

    def get_earnings_forecast(self):
        return self._endpoint('earnings-forecast')

    def get_peg_ratio(self):
        return self._endpoint('peg-ratio')
