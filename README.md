# wharfie-aws

```
brew install pipenv
pipenv --python 3.7
pipenv --where
pipenv --venv
pipenv --py
pipenv install
pipenv shell
which python
python -V
python -c "import boto3"
pip list
exit
```

```
vi ~/.aws/credentials
    [abcd]
    aws_access_key_id = <access_key>
    aws_secret_access_key = <access_key_secret>

vi ~/.aws/config
    [profile abcd]
    region = ap-southeast-2
    output = json

export AWS_PROFILE=abcd
```

```
aws s3 ls
python -m s3.list_buckets
```

```
export BUCKET_NAME=<bucket_name>
python -m s3.list_objects
```

```
export BUCKET_NAME=<bucket_name>
python -m s3.delete_objects
```
