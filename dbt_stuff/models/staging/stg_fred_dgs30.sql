SELECT 
date::DATE,
value AS dgs30
FROM read_parquet("s3://bronze-bucket/fred/series=DGS30/data.parquet", hive_partitioning=true)