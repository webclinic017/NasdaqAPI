import nasdaq as nd
from nasdaq import Frequency # Annual or quarterly, used in financials data

stock = nd.Stock('MSFT')
print(stock.quote.get_realtime_trades(10))
print(stock.quote.get_info())
print(stock.quote.get_dividends())

print(stock.company.get_company_profile())
print(stock.company.get_insider_trades())
print(stock.company.get_financials(Frequency.QUARTERLY))

print(stock.analyst.get_peg_ratio())
print(stock.analyst.get_earnings_forecast())
print(stock.analyst.get_estimate_momentum())

etf = nd.Etf('SPY')

print(etf.quote.get_info())
print(etf.quote.get_dividends())
