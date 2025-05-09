import argparse
import sys
from polygon import RESTClient
import json

#using sys
# n = len(sys.argv)
# print(f"Number of arguments: {n}")
# print(f"Argument List: {sys.argv}")
# [progam, x, y] = sys.argv
# print("total is ", int(x) + int(y))

#using argparse


parser = argparse.ArgumentParser()
parser.add_argument("name", type=str, help="ticker name")

args = parser.parse_args()




# docs
# https://polygon.io/docs/stocks/get_v3_reference_tickers__ticker
# https://polygon-api-client.readthedocs.io/en/latest/Reference.html#get-ticker-details

client = RESTClient("j0ipMPp_4w_LHhIFGJxd0Un8s_AE2FLQ") # hardcoded api_key is used
#client = RESTClient()  # POLYGON_API_KEY environment variable is used

stock = client.get_daily_open_close_agg(args.name, "2025-02-07")

print("open price ->",stock.open, " \nclose price ->", stock.close, "\nhigh price ->", stock.high, "\nlow price->", stock.low)
