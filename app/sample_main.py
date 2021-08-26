import boto3
from boto3.dynamodb.conditions import Attr, Key


def moto_dynamo_sample_main(hoge_id: str) -> None:
    """サンプルアプリ"""

    dynamodb = boto3.resource("dynamodb", region_name="ap-northeast-1")
    dynamo_table = dynamodb.Table("sample_table")

    # レコードを取得
    response = dynamo_table.query(
        KeyConditionExpression=Key("hoge_id").eq(hoge_id),
        FilterExpression=Attr("ym").eq("202006"),
        ScanIndexForward=False,
        Limit=1,
    )

    # 取得したデータを加工して新規に追加する
    update_data = response["Items"][0]
    update_data["seq"] = update_data["seq"] + 1
    update_data["data1"] = "foobar"

    # dynamo書き込み
    dynamo_table.put_item(Item=update_data)
