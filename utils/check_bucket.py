# Checks bucket existence

import boto3
from botocore.exceptions import ClientError

BUCKET_NAME = "bronze-bucket"
ENDPOINT_URL = "http://localhost:4566"


def bucket_exists(s3, bucket_name):
    try:
        s3.head_bucket(Bucket=bucket_name)
        return True
    except ClientError:
        return False


def main():
    s3 = boto3.client(
        "s3",
        endpoint_url=ENDPOINT_URL,
        aws_access_key_id="test",
        aws_secret_access_key="test",
        region_name="us-east-1",
    )

    if bucket_exists(s3, BUCKET_NAME):
        print(f"'{BUCKET_NAME}' exists.")
    else:
        print(f"'{BUCKET_NAME}' does NOT exist.")


if __name__ == "__main__":
    main()