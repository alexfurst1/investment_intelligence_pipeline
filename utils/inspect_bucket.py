# Checks files and file sizes in bucket.

import boto3
import duckdb
import argparse

ENDPOINT = "http://localhost:4566"
BUCKET = "bronze-bucket"

s3 = boto3.client("s3", endpoint_url=ENDPOINT,
                  aws_access_key_id="test", aws_secret_access_key="test")

r = s3.list_objects_v2(Bucket=BUCKET)
print("KeyCount:", r.get("KeyCount"))

files = [
        (obj["Key"], obj['Size'])
        for obj in s3.list_objects_v2(Bucket=BUCKET).get("Contents", [])
        if obj["Key"].endswith(".parquet")
    ]

for key, size in files:
    print(f"{key}, {size:,} bytes")

# KeyCount is the number of files in the bucket.
# obj["Size"] will return the size of the file in bytes.

def inspect():

    # duckdb connection pointed at localstack
    con = duckdb.connect()
    con.sql("INSTALL httpfs; LOAD httpfs;")
    con.sql(f"""
        SET s3_endpoint='localhost:4566';
        SET s3_access_key_id='test';
        SET s3_secret_access_key='test';
        SET s3_use_ssl=false;
        SET s3_url_style='path';
    """)

    for key, size in files:
        path = f"s3://{BUCKET}/{key}"
        print(f"\n=== {key} ===")

        # columns + types
        cols = con.sql(f"DESCRIBE SELECT * FROM read_parquet('{path}')").df()
        print(cols[["column_name", "column_type"]].to_string(index=False))

        # row count
        rows = con.sql(f"SELECT COUNT(*) AS n FROM read_parquet('{path}')").fetchone()[0]
        print(f"rows: {rows}")

        # date range (assumes a 'date' column exists)
        try:
            rng = con.sql(
                f"SELECT MIN(date) AS earliest, MAX(date) AS latest "
                f"FROM read_parquet('{path}')"
            ).fetchone()
            print(f"range: {rng[0]} -> {rng[1]}")
        except Exception:
            print("range: (no 'date' column)")

parser = argparse.ArgumentParser()
parser.add_argument("--task", choices=['inspect'])
args = parser.parse_args()

if args.task == "inspect":
    inspect()