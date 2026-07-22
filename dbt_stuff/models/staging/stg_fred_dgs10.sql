SELECT
    date::DATE AS date, 
    value AS dgs10
FROM read_parquet("s3://bronze-bucket/fred/series=DGS10/data.parquet", hive_partitioning=true)