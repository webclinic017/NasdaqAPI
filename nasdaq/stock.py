from .analyst import Analyst
from .company import Company
from .quote import Quote


class Stock:
    def __init__(self, ticker):
        self.ticker = ticker.upper()
        self.company = Company(ticker=ticker)
        self.quote = Quote(ticker=ticker, assetclass='stocks')
        self.analyst = Analyst(ticker=ticker)
