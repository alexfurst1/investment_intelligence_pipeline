SELECT
date::DATE,
close AS spy_close, high AS spy_high, low AS spy_low, open AS spy_open, volume AS spy_volume
FROM read_parquet("s3://bronze-bucket/yfinance/series=SPY/data.parquet", hive_partitioning=true)