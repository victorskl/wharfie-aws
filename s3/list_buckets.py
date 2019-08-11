import boto3

"""List all S3 buckets

API:
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#service-resource
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.ServiceResource.buckets

REF:
https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html

"""

s3 = boto3.resource('s3')

# Print out bucket names
for bucket in s3.buckets.all():
    print(bucket.name)
