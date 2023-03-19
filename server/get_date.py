from datetime import date

def get_date():
  # YYYY-MM-DD
  today = date.today()
  # YYYY-MMM-DD
  formatted_date = today.strftime('%Y-%b-%d')

  print('Today\'s date is:', today)
  return today