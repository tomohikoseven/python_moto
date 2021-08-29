import logging
import sys

import boto3
from botocore.exceptions import ClientError

#import queue_wrapper


logger = logging.getLogger(__name__)
sqs = boto3.resource("sqs")

def send_message(queue, message_body, message_attributes=None):
  if not message_attributes:
    message_attributes = {}

  try:
    response = queue.send_message(
      MessageBody = message_body,
      MessageAttributes = message_attributes
    )

  except ClientError as error:
    logger.exception("Send message failed: %s", message_body)
    raise error
  else:
    return response