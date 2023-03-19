import csv
import pandas as pd
import numpy as np
import math
from crawl import crawl
from get_owner_list import get_owner_list
from update_watch_list import update_watch_list
from output_csv import output_csv

def start():
  print("start() starts")
  WATCH_LIST = './data/watch_list.csv'
  df = pd.read_csv(WATCH_LIST)
  
  for row in df.values:
    result = {
    'update': False,
    'stock_name': '',
    'latest_no_of_txn': '',
    'lastest_txn_date': '',
    'dataframe': math.nan
    }
    CIK = row[2]
    print("\nprocessing ", CIK)
    last_txn_date = row[2]
    no_of_txn = row[3]
    
    get_owner_list(CIK)
    result = crawl(CIK, no_of_txn, last_txn_date)
    if (result['update']):
      output_csv(result)
      update_watch_list(CIK, result)
  
  print("start() ends")
    
# math.isnan(obj)