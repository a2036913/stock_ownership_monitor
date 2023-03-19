import math
import numpy as np
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

def crawl(CIK, last_no_of_txn, last_txn_date):
  data = []
  result = {
  'update': False,
  'stock_name': '',
  'latest_no_of_txn': '',
  'lastest_txn_date': '',
  'dataframe': math.nan
  }
  latest_no_of_txn = 0
  
  # URL
  url = f'https://www.sec.gov/cgi-bin/own-disp?action=getissuer&CIK={CIK}'
  response = requests.get(url)
  html_content = response.content
  # Parse the HTML content
  soup = bs(html_content, 'html.parser')
  
  # Find stock name and CIK
  tables = soup.find_all('table')
  info_row = tables[3].find_all('td')[0]
  stock_name = info_row.find('b').text.strip().split("(")[0]
  stock_CIK = info_row.find('a').text.strip()
  # get table data
  records = soup.find('table' ,{'id': 'transaction-report'})
  rows = records.find_all('tr')
  # find record header
  header = rows[0]
  header_cols = header.find_all('th')
  header_cols = [col.text.strip() for col in header_cols]
  header_cols.append("doc link")
  rows.pop(0)
  # append records to data
  for row in rows:
    cols = row.find_all('td')
    cols = [col.text.strip() for col in cols]
    link = "https://www.sec.gov" + row.find('a').get('href')
    cols.append(link)
    data.append(cols)
    # get last record
    if(row == rows[0]):
      latest_txn_date = cols[1]

  # output to dataframe
  df = pd.DataFrame(data, columns=header_cols)
  filter_records = df[df["Transaction Date"] == latest_txn_date]
  latest_no_of_txn = len(filter_records.index)
  print("Number of txn on", latest_txn_date, ": ", 
        latest_no_of_txn)
  
  # check should update watch_list.csv
  if (latest_no_of_txn != last_no_of_txn and latest_txn_date != last_txn_date):
    result = {
    'update': True,
    'stock_name': stock_name,
    'latest_no_of_txn': latest_no_of_txn,
    'lastest_txn_date': latest_txn_date,
    'dataframe': df
    }
  
  print("crawl() ends")
  return result