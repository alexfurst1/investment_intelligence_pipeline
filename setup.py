from ingestion import s3_client

s3_client.ensure_bucket(s3_client.s3, "bronze_bucket")