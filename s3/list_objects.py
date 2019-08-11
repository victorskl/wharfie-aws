import os

import boto3

"""List all objects with versions from a bucket

API:
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#bucket
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Bucket.objects
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Bucket.object_versions

"""

if 'BUCKET_NAME' in os.environ:
    s3 = boto3.resource('s3')
    bucket = s3.Bucket(os.environ.get('BUCKET_NAME'))

    for obj in bucket.objects.all():
        print(obj)

    for obj_ver in bucket.object_versions.all():
        print(obj_ver)
else:
    print('Please set environment variable BUCKET_NAME')
