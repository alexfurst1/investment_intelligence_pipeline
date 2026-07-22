SELECT 
date::DATE AS date,
value AS cpiaucsl
FROM read_parquet("s3://bronze-bucket/fred/series=CPIAUCSL/data.parquet", hive_partitioning=true)