## nasdaq.com unofficial API

### Todo list

- [x] ETFs support
- [x] Stocks support  
- [ ] Add more functionalities
- [ ] Integrate with Pandas, Matplotlib
- [ ] Handle errors, server errors
- [ ] Support indexes, crypto
- [ ] Parse responses
- [ ] Support multiple tickers
- [ ] A lot more

### Usage
```python
import nasdaq as nd

stock = nd.Stock('MSFT')
```


```python
stock.quote.get_info()
```




    {'symbol': 'MSFT',
     'companyName': 'Microsoft Corporation Common Stock',
     'stockType': 'Common Stock',
     'exchange': 'NASDAQ-GS',
     'isNasdaqListed': True,
     'isNasdaq100': True,
     'isHeld': False,
     'primaryData': {'lastSalePrice': '$230.20',
      'netChange': '-1.40',
      'percentageChange': '-0.60%',
      'deltaIndicator': 'down',
      'lastTradeTimestamp': 'DATA AS OF Mar 08, 2021 8:26 AM ET - PRE-MARKET',
      'isRealTime': True},
     'secondaryData': {'lastSalePrice': '$231.60',
      'netChange': '+4.87',
      'percentageChange': '+2.15%',
      'deltaIndicator': 'up',
      'lastTradeTimestamp': 'CLOSED AT 4:00 PM ET ON Mar 05, 2021',
      'isRealTime': False},
     'keyStats': {'Volume': {'label': 'Volume', 'value': '94,043'},
      'PreviousClose': {'label': 'Previous Close', 'value': '$231.60'},
      'OpenPrice': {'label': 'Open', 'value': '$229.50'},
      'MarketCap': {'label': 'Market Cap', 'value': '1,746,777,171,637'}},
     'marketStatus': 'Pre Market',
     'assetClass': 'STOCKS',
     'tradingHeld': None,
     'complianceStatus': None}




```python
stock.quote.get_dividends()
```




    {'exDividendDate': '02/17/2021',
     'dividendPaymentDate': '03/11/2021',
     'yield': '0.98%',
     'annualizedDividend': '2.24',
     'payoutRatio': '34.52',
     'dividends': {'headers': {'exOrEffDate': 'Ex/EFF DATE',
       'type': 'TYPE',
       'amount': 'CASH AMOUNT',
       'declarationDate': 'DECLARATION DATE',
       'recordDate': 'RECORD DATE',
       'paymentDate': 'PAYMENT DATE'},
      'rows': [{'exOrEffDate': '02/17/2021',
        'type': 'CASH',
        'amount': '$0.56',
        'declarationDate': '12/02/2020',
        'recordDate': '02/18/2021',
        'paymentDate': '03/11/2021'},
       {'exOrEffDate': '11/18/2020',
        'type': 'CASH',
        'amount': '$0.56',
        'declarationDate': '09/15/2020',
        'recordDate': '11/19/2020',
        'paymentDate': '12/10/2020'},
       {'exOrEffDate': '08/19/2020',
        'type': 'CASH',
        'amount': '$0.51',
        'declarationDate': '06/17/2020',
        'recordDate': '08/20/2020',
        'paymentDate': '09/10/2020'}]}}
        --- snip ---




```python
stock.company.get_company_profile()
```




    {'ModuleTitle': {'label': 'Module Title', 'value': 'Company Description'},
     'CompanyName': {'label': 'Company Name', 'value': 'Microsoft Corporation'},
     'Symbol': {'label': 'Symbol', 'value': 'MSFT'},
     'Address': {'label': 'Address',
      'value': 'ONE MICROSOFT WAY, REDMOND, Washington, 98052-6399, United States of America'},
     'Phone': {'label': 'Phone', 'value': '4258828080'},
     'Industry': {'label': 'Industry',
      'value': 'Computer Software: Prepackaged Software'},
     'Sector': {'label': 'Sector', 'value': 'Technology'},
     'Region': {'label': 'Region', 'value': 'North America'},
     'CompanyDescription': {'label': 'Company Description',
      'value': 'This report includes estimates, projections, statements relating to our business\r\nplans, objectives, and expected operating results that are "forward-looking\r\nstatements" within the meaning of the Private Securities Litigation Reform Act\r\nof 1995, Section 27A of the Securities Act of 1933, and Section 21E of the\r\nSecurities Exchange Act of 1934. Forward-looking statements may appear\r\nthroughout this report, including the following sections: "Business" (Part I,\r\nItem 1 of this Form 10-K), "Risk Factors" (Part I, Item 1A of this Form 10-K),\r\nand "Management\'s Discussion and Analysis of Financial Condition and Results of\r\nOperations" (Part II, Item 7 of this Form 10-K). These forward-looking\r\nstatements generally are identified by the words "believe," "project," "expect,"\r\n"anticipate," "estimate," "intend," "strategy," "future," "opportunity," "plan,"\r\n"may," "should," "will," "would," "will be," "will continue," "will likely\r\nresult," and similar expressions.&nbsp;&nbsp;... <a href="http://secfilings.nasdaq.com/edgar_conv_html%2f2019%2f08%2f01%2f0001564590-19-027952.html#FIS_BUSINESS" target="_blank">More</a> ...&nbsp;&nbsp;\r\n'},
     'CompanyUrl': {'label': 'Company Url', 'value': 'http://www.microsoft.com'},
     'KeyExecutives': {'label': 'Key Executives',
      'value': [{'name': 'Amy E. Hood',
        'title': 'Chief Financial Officer & Executive Vice President'},
       {'name': 'Bill Duff', 'title': 'CFO-Operating Systems Group'},
       {'name': "David M. O'Hara",
        'title': 'Chief Financial Officer-Online Services Division'},
       {'name': 'James Kevin Scott',
        'title': 'Chief Technology Officer & Executive VP'},
       {'name': 'Kirk Koenigsbauer',
        'title': 'COO & VP-Experiences & Devices Group'},
       {'name': 'Satya Nadella',
        'title': 'Chief Executive Officer & Non-Independent Director'}]}}




```python
stock.company.get_insider_trades()
```




    {'title': None,
     'numberOfTrades': {'headers': {'insiderTrade': 'INSIDER TRADE',
       'months3': '3 MONTHS',
       'months12': '12 MONTHS'},
      'rows': [{'insiderTrade': 'Number of Open Market Buys',
        'months3': '7',
        'months12': '40'},
       {'insiderTrade': 'Number of Sells', 'months3': '14', 'months12': '47'},
       {'insiderTrade': 'Total Insider Trades',
        'months3': '21',
        'months12': '87'}]},
     'numberOfSharesTraded': {'headers': {'insiderTrade': 'INSIDER TRADE',
       'months3': '3 MONTHS',
       'months12': '12 MONTHS'},
      'rows': [{'insiderTrade': 'Number of Shares Bought',
        'months3': '901,296',
        'months12': '1,879,369'},
       {'insiderTrade': 'Number of Shares Sold',
        'months3': '726,316',
        'months12': '1,747,708'},
       {'insiderTrade': 'Total Shares Traded',
        'months3': '1,627,612',
        'months12': '3,627,077'},
       {'insiderTrade': 'Net Activity',
        'months3': '174,980',
        'months12': '131,661'}]},
     'transactionTable': {'totalRecords': '201',
      'table': {'headers': {'insider': 'INSIDER',
        'relation': 'RELATION',
        'lastDate': 'LAST DATE',
        'transactionType': 'TRANSACTION',
        'ownType': 'OWNER TYPE',
        'sharesTraded': 'SHARES TRADED',
        'lastPrice': 'PRICE',
        'sharesHeld': 'SHARES HELD'},
       'rows': [{'insider': 'NADELLA SATYA',
         'relation': 'Officer',
         'lastDate': '03/02/2021',
         'transactionType': 'Automatic Sell',
         'ownType': 'Direct',
         'sharesTraded': '278,694',
         'lastPrice': '$234.12',
         'sharesHeld': '1,345,661',
         'url': '/market-activity/insiders/nadella-satya-848613'},
        {'insider': 'CAPOSSELA CHRISTOPHER C',
         'relation': 'Officer',
         'lastDate': '03/01/2021',
         'transactionType': 'Disposition (Non Open Market)',
         'ownType': 'Direct',
         'sharesTraded': '2,736',
         'lastPrice': '$232.38',
         'sharesHeld': '102,968',
         'url': '/market-activity/insiders/capossela-christopher-c-929488'},
        {'insider': 'COURTOIS JEAN PHILIPPE',
         'relation': 'Officer',
         'lastDate': '03/01/2021',
         'transactionType': 'Disposition (Non Open Market)',
         'ownType': 'Direct',
         'sharesTraded': '6,006',
         'lastPrice': '$232.38',
         'sharesHeld': '587,909',
         'url': '/market-activity/insiders/courtois-jean-philippe-385537'},
        {'insider': 'HOGAN KATHLEEN T',
         'relation': 'Officer',
         'lastDate': '03/01/2021',
         'transactionType': 'Disposition (Non Open Market)',
         'ownType': 'Direct',
         'sharesTraded': '3,671',
         'lastPrice': '$232.38',
         'sharesHeld': '185,393',
         'url': '/market-activity/insiders/hogan-kathleen-t-951115'},
        {'insider': 'HOOD AMY',
         'relation': 'Officer',
         'lastDate': '03/01/2021',
         'transactionType': 'Disposition (Non Open Market)',
         'ownType': 'Direct',
         'sharesTraded': '7,508',
         'lastPrice': '$232.38',
         'sharesHeld': '477,359',
         'url': '/market-activity/insiders/hood-amy-906897'},
        {'insider': 'JOLLA ALICE L.',
         'relation': 'Officer',
         'lastDate': '03/01/2021',
         'transactionType': 'Disposition (Non Open Market)',
         'ownType': 'Direct',
         'sharesTraded': '592',
         'lastPrice': '$232.38',
         'sharesHeld': '57,935',
         'url': '/market-activity/insiders/jolla-alice-l-1124486'},
        {'insider': 'NADELLA SATYA',
         'relation': 'Officer',
         'lastDate': '03/01/2021',
         'transactionType': 'Disposition (Non Open Market)',
         'ownType': 'Direct',
         'sharesTraded': '14,868',
         'lastPrice': '$232.38',
         'sharesHeld': '1,923,555',
         'url': '/market-activity/insiders/nadella-satya-848613'},
        {'insider': 'SMITH BRADFORD L',
         'relation': 'Officer',
         'lastDate': '03/01/2021',
         'transactionType': 'Disposition (Non Open Market)',
         'ownType': 'Direct',
         'sharesTraded': '5,917',
         'lastPrice': '$232.38',
         'sharesHeld': '702,584',
         'url': '/market-activity/insiders/smith-bradford-l-383020'},
        {'insider': 'NADELLA SATYA',
         'relation': 'Officer',
         'lastDate': '02/10/2021',
         'transactionType': 'Acquisition (Non Open Market)',
         'ownType': 'Direct',
         'sharesTraded': '900,000',
         'lastPrice': '$0.00',
         'sharesHeld': '2,292,573',
         'url': '/market-activity/insiders/nadella-satya-848613'},
        {'insider': 'NADELLA SATYA',
         'relation': 'Officer',
         'lastDate': '02/10/2021',
         'transactionType': 'Disposition (Non Open Market)',
         'ownType': 'Direct',
         'sharesTraded': '354,150',
         'lastPrice': '$243.77',
         'sharesHeld': '1,938,423',
         'url': '/market-activity/insiders/nadella-satya-848613'}]}},
     'filerTransactionTable': None}




```python
stock.analyst.get_peg_ratio()
```




    {'pegr': {'label': 'Forecast 12 Month Forward PEG Ratio',
      'text': 'Investors are always looking for companies with good growth prospects selling at attractive prices. One popular statistic used to identify such stocks is the PEG ratio - which is simply the Price Earnings ratio divided by the growth rate. In this case we use the forecasted growth rate (based on the consensus of professional analysts) and forecasted earnings over the next 12 months. In theory, the lower the PEG ratio the better - implying that you are paying less for future earnings growth. The PEG ratio for this company is based on expected earnings for twelve months ending <b>February 2022</b>',
      'pegValue': 2.64},
     'per': {'peRatioChart': [{'x': '2020 Actual', 'y': 40.21},
       {'x': '2021 Estimates', 'y': 31.55},
       {'x': '2022 Estimates', 'y': 28.84},
       {'x': '2023 Estimates', 'y': 25.82}],
      'label': 'Price/Earnings Ratio',
      'text': 'Price/Earnings Ratio is a widely used stock evaluation measure. For a security, the Price/Earnings Ratio is given by dividing the Last Sale Price by the Average EPS (Earnings Per Share) Estimate for the specified fiscal time period.',
      'dataProvider': '<b>Data Provider:</b> Data is er by Zacks Investment Research'},
     'gr': {'peGrowthChart': [{'z': 'Growth', 'x': '2021', 'y': 27.41},
       {'z': 'Growth', 'x': '2022', 'y': 9.48},
       {'z': 'P/E Ratios', 'x': '2021', 'y': 31.55},
       {'z': 'P/E Ratios', 'x': '2022', 'y': 28.84}],
      'title': 'Forecast P/E Growth Rates'}}




```python
stock.analyst.get_earnings_forecast()
```




    {'symbol': 'msft',
     'quarterlyForecast': {'headers': {'fiscalEnd': 'Fiscal Quarter End',
       'consensusEPSForecast': 'Consensus EPS* Forecast',
       'highEPSForecast': 'High EPS* Forecast',
       'lowEPSForecast': 'Low EPS* Forecast',
       'noOfEstimates': 'Number of Estimates',
       'up': 'Over the Last 4 Weeks Number of Revisions - Up',
       'down': 'Over the Last 4 Weeks Number of Revisions - Down'},
      'rows': [{'fiscalEnd': 'Mar 2021',
        'consensusEPSForecast': 1.76,
        'highEPSForecast': 1.83,
        'lowEPSForecast': 1.69,
        'noOfEstimates': 14,
        'up': 0,
        'down': 0},
       {'fiscalEnd': 'Jun 2021',
        'consensusEPSForecast': 1.76,
        'highEPSForecast': 1.85,
        'lowEPSForecast': 1.68,
        'noOfEstimates': 12,
        'up': 0,
        'down': 0},
       {'fiscalEnd': 'Sep 2021',
        'consensusEPSForecast': 1.91,
        'highEPSForecast': 2.05,
        'lowEPSForecast': 1.69,
        'noOfEstimates': 10,
        'up': 0,
        'down': 0},
       {'fiscalEnd': 'Dec 2021',
        'consensusEPSForecast': 2.11,
        'highEPSForecast': 2.32,
        'lowEPSForecast': 1.87,
        'noOfEstimates': 10,
        'up': 0,
        'down': 0},
       {'fiscalEnd': 'Mar 2022',
        'consensusEPSForecast': 1.96,
        'highEPSForecast': 2.13,
        'lowEPSForecast': 1.76,
        'noOfEstimates': 10,
        'up': 0,
        'down': 0}]},
     'yearlyForecast': {'headers': {'fiscalEnd': 'Fiscal Year End',
       'consensusEPSForecast': 'Consensus EPS* Forecast',
       'highEPSForecast': 'High EPS* Forecast',
       'lowEPSForecast': 'Low EPS* Forecast',
       'noOfEstimates': 'Number of Estimates',
       'up': 'Over the Last 4 Weeks Number of Revisions - Up',
       'down': 'Over the Last 4 Weeks Number of Revisions - Down'},
      'rows': [{'fiscalEnd': 'Jun 2021',
        'consensusEPSForecast': 7.34,
        'highEPSForecast': 7.53,
        'lowEPSForecast': 6.98,
        'noOfEstimates': 15,
        'up': 0,
        'down': 0},
       {'fiscalEnd': 'Jun 2022',
        'consensusEPSForecast': 8.03,
        'highEPSForecast': 8.56,
        'lowEPSForecast': 7.23,
        'noOfEstimates': 15,
        'up': 0,
        'down': 0},
       {'fiscalEnd': 'Jun 2023',
        'consensusEPSForecast': 8.97,
        'highEPSForecast': 9.91,
        'lowEPSForecast': 7.77,
        'noOfEstimates': 7,
        'up': 0,
        'down': 0},
       {'fiscalEnd': 'Jun 2024',
        'consensusEPSForecast': 10.62,
        'highEPSForecast': 10.62,
        'lowEPSForecast': 10.62,
        'noOfEstimates': 1,
        'up': 0,
        'down': 0}]}}




```python
stock.analyst.get_estimate_momentum()
```




    {'symbol': 'msft',
     'changeInConsensus': {'monthData': {'period': '1 Month \n Ago',
       'qtrMean': 1.76,
       'yrMean': 7.34},
      'weekData': {'period': '1 Week \n Ago', 'qtrMean': 1.76, 'yrMean': 7.34},
      'currentData': {'period': 'Current', 'qtrMean': 1.76, 'yrMean': 7.34},
      'fiscalYearEndText': 'Fiscal Year End Jun 2021',
      'fiscalQtrEndText': 'Fiscal Quarter End Mar 2021'},
     'estimatesChanged': {'quarterDataDown': {'changeType': 'Down',
       'changeValue': 0},
      'quarterDataUp': {'changeType': 'Up', 'changeValue': 0},
      'yearDataDown': {'changeType': 'Down', 'changeValue': 0},
      'yearDataUp': {'changeType': 'Up', 'changeValue': 0},
      'qtrFiscalQtrEndText': 'Fiscal QE Mar 2021',
      'yrFiscalYearEndText': 'Fiscal YR Jun 2021'},
     'textInfo': 'Estimate Momentum measures change in analyst sentiment over time and may be an indicator of future price movements. The Change in Consensus chart shows the current, 1 week ago, and 1 month ago consensus earnings per share (EPS*) forecasts.\n For the fiscal quarter endingMar 2021 , the consensus EPS* forecast has remained the same over the past week at 1.76 and remained the same over the past month at 1.76. none raised and none lowered their forecast.\n For the fiscal year ending Jun 2021 , the consensus EPS* forecast has remained the same over the past week at 7.34 and remained the same over the past month at 7.34 . none raised and none lowered their forecast.'}




```python
etf = nd.Etf('SPY')
```


```python
etf.quote.get_info()
```




    {'symbol': 'SPY',
     'companyName': 'SPDR S&P 500',
     'stockType': 'Exchange Traded Fund',
     'exchange': 'PSE',
     'isNasdaqListed': False,
     'isNasdaq100': False,
     'isHeld': False,
     'primaryData': {'lastSalePrice': '$382.93',
      'netChange': '-0.70',
      'percentageChange': '-0.18%',
      'deltaIndicator': 'down',
      'lastTradeTimestamp': 'DATA AS OF Mar 08, 2021 8:26 AM ET - PRE-MARKET',
      'isRealTime': True},
     'secondaryData': {'lastSalePrice': '$383.63',
      'netChange': '+6.93',
      'percentageChange': '+1.84%',
      'deltaIndicator': 'up',
      'lastTradeTimestamp': 'CLOSED AT 4:00 PM ET ON Mar 05, 2021',
      'isRealTime': False},
     'keyStats': {'Volume': {'label': 'Volume', 'value': '518,299'},
      'ExpenseRatio': {'label': 'Expense Ratio', 'value': '0.09%'},
      'AUM': {'label': 'Assets Under Management', 'value': '326,679,520'},
      'AverageSpread': {'label': 'Average Spread', 'value': 'N/A'}},
     'marketStatus': 'Pre Market',
     'assetClass': 'ETF',
     'tradingHeld': None,
     'complianceStatus': None}




```python
etf.quote.get_dividends()
```




    {'exDividendDate': '12/18/2020',
     'dividendPaymentDate': '01/29/2021',
     'yield': '1.49%',
     'annualizedDividend': '5.691',
     'payoutRatio': 'N/A',
     'dividends': {'headers': {'exOrEffDate': 'Ex/EFF DATE',
       'type': 'TYPE',
       'amount': 'CASH AMOUNT',
       'declarationDate': 'DECLARATION DATE',
       'recordDate': 'RECORD DATE',
       'paymentDate': 'PAYMENT DATE'},
      'rows': [{'exOrEffDate': '12/18/2020',
        'type': 'CASH',
        'amount': '$1.58',
        'declarationDate': '01/16/2020',
        'recordDate': '12/21/2020',
        'paymentDate': '01/29/2021'},
       {'exOrEffDate': '09/18/2020',
        'type': 'CASH',
        'amount': '$1.339',
        'declarationDate': '01/16/2020',
        'recordDate': '09/21/2020',
        'paymentDate': '10/30/2020'}]}}
        --- snip ---