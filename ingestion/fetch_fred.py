from fredapi import Fred
import os

fred = Fred(api_key=os.getenv('FRED_API_KEY'))

print(fred.get_series("UNRATE",frequency="a"))