SELECT
date::DATE AS date,
value AS unrate
FROM read_parquet("s3://bronze-bucket/fred/series=UNRATE/data.parquet", hive_partitioning=true)