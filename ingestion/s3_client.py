import boto3

s3 = boto3.client(
    "s3",
    endpoint_url="http://localhost:4566",
    aws_access_key="test",
    aws_secret_key="test",
    region_name="us-east-1"
)

def ensure_bucket(s3, bucket_name):
    existing = [b["Name"] for b in s3.list_buckets()["Buckets"]]
    if bucket_name not in existing:
        s3.create_bucket(Bucket=bucket_name)
    else:
        print("S3 bucket exists.")
