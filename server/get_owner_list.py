import pandas as pd
from bs4 import BeautifulSoup as bs
import requests

def get_owner_list(CIK):
  data = []
  # request
  url = f'https://www.sec.gov/cgi-bin/own-disp?action=getissuer&CIK={CIK}'
  print('get_owner_list, url: ', url)
  
  response = requests.get(url)
  html_content = response.content
  soup = bs(html_content, 'html.parser')
  # get table
  tables = soup.find_all('table')
  
  info_row = tables[3].find_all('td')[0]
  stock_name = info_row.find('b').text.strip().split("(")[0]
  owner_table = tables[5].find_all('tr')
  
  # get header
  header = owner_table[0].find_all('td')
  header = [str(col).strip() for col in header]
  
  # get owners list
  owner_table.pop(0)
  for row in owner_table:
    cols = row.find_all('td')
    cols = [col.Text.strip() for col in cols]
    data.append(cols)

  # output csv file
  df = pd.DataFrame(data, columns=header)
  df.to_csv(f'./data/{stock_name}_owner_list.csv')
  print("output_owner_list.py ends")