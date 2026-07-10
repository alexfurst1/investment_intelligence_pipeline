# Checks files and file sizes in bucket.

import boto3

s3 = boto3.client("s3", endpoint_url="http://localhost:4566",
                  aws_access_key_id="test", aws_secret_access_key="test")

r = s3.list_objects_v2(Bucket="bronze-bucket")
print("KeyCount:", r.get("KeyCount"))

for obj in s3.list_objects_v2(Bucket="bronze-bucket").get("Contents", []):
    print(obj["Key"], obj["Size"])

# KeyCount is the number of files in the bucket.
# obj["Size"] will return the size of the file in bytes.