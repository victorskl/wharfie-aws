import os

import boto3

"""Delete all objects and their versions from a bucket

API:
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#bucket
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Bucket.objects
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Bucket.object_versions

REF:
https://docs.aws.amazon.com/AmazonS3/latest/dev/delete-or-empty-bucket.html
https://stackoverflow.com/questions/43326493/what-is-the-fastest-way-to-empty-s3-bucket-using-boto3

"""

if 'BUCKET_NAME' in os.environ:
    s3 = boto3.resource('s3')
    bucket = s3.Bucket(os.environ.get('BUCKET_NAME'))
    bucket.objects.all().delete()
    bucket.object_versions.delete()
else:
    print('Please set environment variable BUCKET_NAME')
