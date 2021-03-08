from nasdaq.base import Base
from nasdaq.quote import Quote


class Etf(Base):
    def __init__(self, ticker):
        super().__init__(ticker)
        self.ticker = ticker.upper()
        self.quote = Quote(ticker, 'etf')
