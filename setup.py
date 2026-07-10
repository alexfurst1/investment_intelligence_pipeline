from ingestion import backfill, s3_client


s3_client.ensure_bucket(s3_client.s3, "bronze-bucket")

backfill.backfill_fred_signals()
backfill.backfill_yfinance_signals()
