import boto3
from moto import mock_sqs
from app.sample_sqs4 import send_message

@mock_sqs
def test_send_message():
  sqs = boto3.resource("sqs")
  queue = sqs.create_queue(QueueName='test')
  message_body = 'Hello sqs!'


  # test
  response = send_message( queue, message_body )

  res_queue = sqs.get_queue_by_name(QueueName='test')
  message = res_queue.receive_messages()
  print(message)

  assert 1 == 1




