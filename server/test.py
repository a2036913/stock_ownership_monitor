import math
import pandas as pd
from get_date import get_date

def test():
  WATCH_LIST = './data/watch_list.csv'
  CIF = '1065280'
  data = []
  data.append(['NETFLIX INC',1065280,'','',''])
  header = ["stock name",	'CIK', 'txn date',	'number of txn',	'program update date']
  df = pd.DataFrame(data, columns=header)
  df.to_csv(WATCH_LIST)
  
  # df['txn date'] = df['txn date'].replace([math.nan], ['test'])
  for index, row in enumerate(df.values):
    if (str(row[1]) == CIF):
      print(index)
      print(row)
      df.at[index,'txn date'] = 'asdasd'
  print('\n',df)
  df.to_csv('./data/watch_list.csv')
  
test()