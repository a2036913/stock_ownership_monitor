def output_csv(result):
  df = result['dataframe']
  stock_name = result['stock_name']
  df.to_csv(f'./data/{stock_name}.csv')
  print("output_csv() ends")