SELECT
date::DATE AS date,
value AS dgs2
FROM read_parquet("s3://bronze-bucket/fred/series=DGS2/data.parquet", hive_partitioning=true)