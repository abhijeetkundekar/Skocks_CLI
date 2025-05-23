import argparse
import sys
from polygon import RESTClient
import json
from utils.env import getClient
from api.stockapi import list_aggs, getAllTickers
from datetime import date
from prettytable import PrettyTable

#using sys
# n = len(sys.argv)
# print(f"Number of arguments: {n}")
# print(f"Argument List: {sys.argv}")
# [progam, x, y] = sys.argv
# print("total is ", int(x) + int(y))

#using argparse


parser = argparse.ArgumentParser()
#parser.add_argument("name", type=str, help="ticker name")
parser.add_argument("-t","--ticker", type=str, help="ticker name")
parser.add_argument("-n","--name", type=str, help="stock name")
parser.add_argument("-st","--start_date", type=str, help="start date in yyyy-mm-dd format")
parser.add_argument("-ed","--end_date", type=str, help="end date", default=date.today().strftime('%Y-%m-%d'))


args = parser.parse_args()

# docs
# https://polygon.io/docs/stocks/get_v3_reference_tickers__ticker
# https://polygon-api-client.readthedocs.io/en/latest/Reference.html#get-ticker-details

#client = RESTClient("j0ipMPp_4w_LHhIFGJxd0Un8s_AE2FLQ") # hardcoded api_key is used
#client = RESTClient()  # POLYGON_API_KEY environment variable is used
#print("args ->", args.ticker)
#stock = client.get_daily_open_close_agg(args.ticker, "2025-05-01")

def checkArgs():
    if args.name == None and args.ticker == None:
        raise Exception("name or ticker is required")  
    if args.start_date == None:
        raise Exception("start date is required")
    if args.ticker and args.start_date:
        getAggs(args.ticker.upper(), args.start_date, args.end_date)
    if args.name and args.start_date:
        getTickersBySearch(args.name)

def getAggs(ticker, start_date, end_date):
    aggs = list_aggs(
        ticker,
        2,
        "day",
        start_date,
        end_date,
        50000,
    )
    table = PrettyTable([ 'Ticker','Open', 'Close', 'High', 'Low'])
    for agg in aggs: 
        table.add_row([ticker,agg.open, agg.close, agg.high, agg.low])
    print(table)

def getTickersBySearch(name):
    result = getAllTickers(name)
    t = PrettyTable(['','Name','Ticker'])
    for index,stock in enumerate(result):
        t.add_row([index+1,stock.name, stock.ticker])
    print(t)
    stockIndex = input("Select a number to select a stock")
    print("selected ->",result[int(stockIndex)-1].ticker)
    getAggs(result[int(stockIndex)-1].ticker, args.start_date, args.end_date)

checkArgs()

#print("ticker ->", stock)
#print("open price ->",stock.open, " \nclose price ->", stock.close, "\nhigh price ->", stock.high, "\nlow price->", stock.low)
