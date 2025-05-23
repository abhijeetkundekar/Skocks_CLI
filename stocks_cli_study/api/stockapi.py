from utils.env import getClient
client = getClient()

def list_aggs(ticker, multiplier, timeStamp, start_date, end_date, limit):
    result = []
    for a in client.list_aggs(
        ticker,
        multiplier,
        timeStamp,
        start_date,
        end_date,
        limit=limit,
    ):
        result.append(a)
    return result
    #return client.list_aggs(ticker, multiplier, timeStamp, start_date, end_date, limit=limit)

def getAllTickers(name):
    tickers = []
    for t in client.list_tickers(
        market="stocks",search=name,active="true",order="asc",limit="100",sort="ticker",
	):
        tickers.append(t)
    return tickers