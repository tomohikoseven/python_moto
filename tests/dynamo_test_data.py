import boto3


def definition_mock_dynamo_table():
    """サンプルDynamoテーブル生成"""

    mock_dynamodb = boto3.resource("dynamodb", region_name="ap-northeast-1")
    mock_table = mock_dynamodb.create_table(
        TableName="sample_table",
        KeySchema=[
            {"AttributeName": "hoge_id", "KeyType": "HASH"},
            {"AttributeName": "seq", "KeyType": "RANGE"},
        ],
        AttributeDefinitions=[
            {"AttributeName": "hoge_id", "AttributeType": "S"},
            {"AttributeName": "seq", "AttributeType": "N"},
        ],
        ProvisionedThroughput={
            "ReadCapacityUnits": 5,
            "WriteCapacityUnits": 5,
        },
    )

    return mock_table


def test_data_01():
    """テストデータ"""
    item = [
        {"hoge_id": "hoge", "ym": "202006", "seq": 1, "data1": "fuga"},
        {"hoge_id": "hoge", "ym": "202006", "seq": 2, "data1": "piyo"},
    ]

    return item