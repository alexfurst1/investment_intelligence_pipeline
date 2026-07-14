from fredapi import Fred
import yfinance as yf
import os

# backfills FRED and yfinance data idempotently. each "to_parquet" method completely rewrites the file path its written to.

def backfill_fred_signals(): 

    fred = Fred(api_key=os.getenv('FRED_API_KEY'))

    # signal id from FRED to be fetched with respective native frequency
    signals = ['DGS2','DGS10','DGS30','UNRATE','CPIAUCSL','FEDFUNDS','GDP']

    for signal in signals:
        try:
            series = fred.get_series(signal)
        except Exception as e:
            print(f"Error: failed to fetch signal: {signal}, e = {e}. Skipping signal.")
            continue

        df = series.to_frame(name="value")
        df.index.name = 'date'
        df = df.reset_index()
        df['series_id'] = signal
        
        try:
            df.to_parquet(
                f's3://bronze-bucket/fred/series={signal}/data.parquet',
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

def backfill_yfinance_signals():
    try:
        df = yf.download('SPY',period='max')
        df = df.reset_index()
        df['source'] = 'SPY'
    except Exception as e:
        print(f"Error: yfinance failed to fetch. e = {e}")
    
    try:
        df.to_parquet(
            f's3://bronze-bucket/yfinance/series=SPY/data.parquet',
            engine='pyarrow',
            storage_options={
                'key':'test',
                'secret':'test',
                'client_kwargs': {'endpoint_url': 'http://localhost:4566'}
                }
        )
    except Exception as e:
        print(f"Error: failed to upload signal: SPY to bucket as parquet. e = {e}.")

# TODO def fetch_signals(): 
            

