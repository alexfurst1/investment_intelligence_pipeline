SELECT
date::DATE,
value AS fedfunds
FROM read_parquet("s3://bronze-bucket/fred/series=FEDFUNDS/data.parquet", hive_partitioning=true)