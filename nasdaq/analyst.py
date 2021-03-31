from nasdaq.base import Base


class Analyst(Base):
    def __init__(self, ticker):
        super().__init__(ticker=ticker, prefix='analyst')

    def get_estimate_momentum(self):
        return self.endpoint('estimate-momentum')

    def get_earnings_forecast(self):
        return self.endpoint('earnings-forecast')

    def get_peg_ratio(self):
        return self.endpoint('peg-ratio')
