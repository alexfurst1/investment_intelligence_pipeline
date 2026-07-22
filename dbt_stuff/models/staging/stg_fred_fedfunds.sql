SELECT
date::DATE AS date,
value AS fedfunds
FROM read_parquet("s3://bronze-bucket/fred/series=FEDFUNDS/data.parquet", hive_partitioning=true)