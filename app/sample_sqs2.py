import boto3

def send_to_sqs( queue_url: str, body: str ):
  sqs_client = boto3.client("sqs")

  response = sqs_client.send_message(
    QueueUrl=queue_url,
    MessageBody=body
  )

  return response["MessageId"]

def receive_from_sqs(queue_url: str) -> (str, str):
  sqs_client = boto3.client("sqs")

  response = sqs_client.reveive_message(QueueUrl=queue_url)

  if "Messages" not in response or len(response["Messages"]) == 0:
    return None, None

  message = response["Messages"][0]

  return message["Body"], message["ReceiptHandle"]