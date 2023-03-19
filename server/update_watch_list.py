import pandas as pd
from datetime import date
from get_date import get_date

def update_watch_list(CIK, result):
  WATCH_LIST = './data/watch_list.csv'
  stock_name = result['stock_name']
  print(stock_name)
  no_of_txn = result['latest_no_of_txn']    
  last_txn_date = result['lastest_txn_date']
  # YYYY-MM-DD
  today = date.today()
  
  df = pd.read_csv(WATCH_LIST)
  for index, row in enumerate(df.values):
    if (str(row[1]) == CIK):
      print(row)
      print(index)
      df.at[index, 'stock name'] = stock_name
      df.at[index, 'txn date'] = last_txn_date
      df.at[index, 'number of txn'] = no_of_txn
      df.at[index, 'program update date'] = today
  df.to_csv('./data/watch_list.csv')
  print("update_watch_list ends")