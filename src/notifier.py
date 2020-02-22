import os
import boto3
from botocore.vendored import requests

def notify(event, context):
    """
    Will take the provided SNS message and publish it to the webhook URL
    located within the environment variables
    """

    client = boto3.client('secretsmanager')
    secret_arn = os.environ['webhook_sm_arn']
    webhook_url = client.get_secret_value(SecretId=secret_arn)

    channel = os.environ['channel']
    message = event["Records"][0]["Sns"]["Message"]
    payload = {
        'text': message,
        'channel': channel,
        'username': 'AWS Alert Notification'
    }
    print('DEBUG:', payload)
    r = requests.post(webhook_url, json=payload)
    return r.status_code