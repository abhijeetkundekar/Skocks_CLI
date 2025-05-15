import argparse
import sys
from polygon import RESTClient
import json
from utils.env import getClient
from datetime import date

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
parser.add_argument("-st","--start_date", type=str, help="start date")
parser.add_argument("-ed","--end_date", type=str, help="end date", default=date.today())


args = parser.parse_args()


# docs
# https://polygon.io/docs/stocks/get_v3_reference_tickers__ticker
# https://polygon-api-client.readthedocs.io/en/latest/Reference.html#get-ticker-details

#client = RESTClient("j0ipMPp_4w_LHhIFGJxd0Un8s_AE2FLQ") # hardcoded api_key is used
#client = RESTClient()  # POLYGON_API_KEY environment variable is used
print("args ->", args)
stock = getClient().get_daily_open_close_agg(args.ticker, "2025-05-01")
print("ticker ->", stock)
print("open price ->",stock.open, " \nclose price ->", stock.close, "\nhigh price ->", stock.high, "\nlow price->", stock.low)
