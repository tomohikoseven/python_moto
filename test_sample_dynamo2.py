import datetime
import pytest
import boto3
from moto import mock_dynamodb2

# テスト対象
from app.sample_dynamo2 import put_to_dynamo, get_from_dynamo

class TestDynamoMethods:

    @mock_dynamodb2
    def test_put_get_succeed(self):
        dynamodb = boto3.resource("dynamodb", region_name="ap-northeast-1")
        dynamodb.create_table(
            TableName="moto-example",
            KeySchema=[{"AttributeName": "user_id", "KeyType": "HASH"}],
            AttributeDefinitions=[{"AttributeName": "user_id", "AttributeType": "N"}],
        )

        put_to_dynamo(user_id=33, access_count=10, last_accessed_at=datetime.datetime(2020, 3, 21, 10, 30, 15))

        item = get_from_dynamo(user_id=33)
        assert item["user_id"] == 33
        assert item["access_count"] == 10
        assert item["last_accessed_at"] == datetime.datetime(2020, 3, 21, 10, 30, 15)