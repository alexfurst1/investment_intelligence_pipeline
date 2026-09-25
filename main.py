from ingestion import backfill, s3_client
from prefect import flow, task
from prefect.schedules import Cron

@flow
def pipeline():
    s3_client.ensure_bucket(s3_client.s3, "bronze-bucket")
    backfill.backfill_fred_signals()
    backfill.backfill_yfinance_signals()
    backfill.run_dbt("build")


if __name__ == "__main__":
    pipeline.serve(
        name="daily_pipeline",
        schedules=[Cron("0 16 * * 1-5", timezone="America/New_York")],
    )