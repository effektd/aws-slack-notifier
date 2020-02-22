# aws-slack-notifier
A basic Slack notification Slack using AWS Lambda and SNS

## About

This is a basic CloudFormation stack that will deploy a lambda to handle SNS published messages and then send them to your nomiated Slack channel for notification.

The stack will securely store your Slack API token in AWS Secrets Manager and store your Slack webhook URL in AWS Systems Manager Parameter Store

## Usage

Standard use case for this CloudFormation stack is quite broad, you can essentially publish any message to the SNS topic and the lambda function will handle the SNS message and send it on to your Slack channel.

The SNS message can be anything you like, you could expand the lambda function to handle certain subjects differently if desired.

## AWS Services used

- AWS CloudFormation
- AWS Lambda
- AWS Secret Manager
- AWS Simple Notification Service
- AWS System Manager Parameter Store