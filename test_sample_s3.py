import pytest
import boto3
from botocore.exceptions import ClientError
from moto import mock_s3

# テスト対象となる関数
from app.sample_s3 import (
    upload_to_bucket, download_from_bucket,
)

bucket = "moto-example"

@mock_s3
def test_s3_bucket():
  bucket_name ='test_bucket'
  client = boto3.client('s3')
  assert client.list_buckets()['Buckets'] == []
  client.create_bucket(
    Bucket=bucket_name
    ,CreateBucketConfiguration={
      'LocationConstraint': 'eu-west-1'
    }
  )
  assert client.list_buckets()['Buckets'][0]['Name'] == bucket_name

@mock_s3
def test_upload_succeed():
  # バケットの生成
  s3 = boto3.resource("s3")
  s3.create_bucket(
    Bucket=bucket
    ,CreateBucketConfiguration={
      'LocationConstraint': 'eu-west-1'
    }
  )

  assert upload_to_bucket("./data/example.txt", "example.txt")

  # アップロードされたファイルをGet
  body = s3.Object(bucket, "data/example.txt").get()["Body"].read().decode("utf-8")

  assert body == "Hello, world!"

@pytest.mark.skip(reason="for debug")
def test_download_failed():
    s3 = boto3.resource("s3")
    s3.create_bucket(Bucket=bucket)

    # botocoreの例外クラスがスローされる
    with pytest.raises(ClientError):
        download_from_bucket("nonexist.txt", "output/example.txt")