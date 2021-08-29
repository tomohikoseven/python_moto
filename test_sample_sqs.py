import pytest
import boto3
from moto import mock_sqs

# テスト対象
from app.sample_sqs import send_to_sqs, receive_from_sqs

@mock_sqs
class TestSqsMethods:
    def setup_method(self, method):
        sqs = boto3.client('sqs')
        response = sqs.create_queue(QueueName="moto-example")
        self.queue_url = response["QueueUrl"]

    def test_send_receive_succeed(self):
        assert send_to_sqs(queue_url=self.queue_url, body="Hello, world!")

        body, receipt_handle = receive_from_sqs(queue_url=self.queue_url)
        assert body == "Hello, world!"
        assert receipt_handle

    def test_receive_empty(self):
        body, receipt_handle = receive_from_sqs(queue_url=self.queue_url)
        assert body is None
        assert receipt_handle is None