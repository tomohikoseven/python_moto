from moto import mock_dynamodb2
from tests.dynamo_test_data import definition_mock_dynamo_table, test_data_01
from boto3.dynamodb.conditions import Attr, Key
from app.sample_main import moto_dynamo_sample_main


class TestSample:

    @mock_dynamodb2
    def test_motoでdynamodbをモックで使用する(self):
        # モック定義
        mock_table = definition_mock_dynamo_table()
        [mock_table.put_item(Item=data) for data in test_data_01()]

        # 処理実行
        moto_dynamo_sample_main("hoge")

        # 結果確認
        response = mock_table.query(
            KeyConditionExpression=Key("hoge_id").eq("hoge"),
            FilterExpression=Attr("ym").eq("202006"),
            ScanIndexForward=False,
            Limit=1,
        )

        assert len(response["Items"]) == 1, "レコード取得件数"

        actual_data = response["Items"][0]

        assert actual_data["hoge_id"] == "hoge"
        assert actual_data["ym"] == "202006"
        assert actual_data["seq"] == 3
        assert actual_data["data1"] == "foobar"