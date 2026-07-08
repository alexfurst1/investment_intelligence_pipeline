from fredapi import Fred
import os

def backfill_signals(): #backfills all FRED series listed in 'signals' up to today, sends to bronze layer s3 bucket.

    fred = Fred(api_key=os.getenv('FRED_API_KEY'))

    signals = ['DSG10','DSG2','DSG30''UNRATE','CPIAUCSL','FEDFUNDS','GDP']

    for signal in signals:
        try:
            series = fred.get_series(signal,frequency="d")
        except Exception as e:
            print(f"Error: failed to fetch signal: {signal}, e = {e}. Skipping signal.")
            continue

        df = series.to_frame(name="value")
        df.index.name = 'date'
        df = df.reset_index()
        
        try:
            df.to_parquet(
            f's3://bronze_bucket/fred/series={signal}/data.parquet',
            engine='pyarrow',
            storage_options={
                'key':'test',
                'secret':'test',
                'client_kwargs': {'endpoint_url': 'http://localhost:4566'}
                }
            )
        except Exception as e:
            print(f"Error: failed to upload signal: {signal} to bucket as parquet. e = {e}. Skipping signal.")
            continue
            

