import os
import boto3
from botocore.vendored import requests

def handler(event, context):
    """
    Will take the provided SNS payload and publish it's message to the Slack 
    webhook URL which is retrieved during execution
    """

    client = boto3.client('secretsmanager')

    # Retrieve the webhook url from AWS Secrets Manager
    secret_arn = os.environ['webhook_sm_arn']
    response = client.get_secret_value(SecretId=secret_arn)
    webhook_url = response['SecretString']

    # Retrieve the message from the SNS payload and generate a JSON payload
    channel = os.environ['channel']
    message = event["Records"][0]["Sns"]["Message"]
    payload = {
        'text': message,
        'channel': channel,
        'username': 'AWS Alert Notification'
    }
    
    # Send the above payload to the Slack webhook
    r = requests.post(webhook_url, json=payload)
    return r.status_code