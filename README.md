# aws-slack-notifier
A basic Slack notification Slack using AWS Lambda and SNS

## About

This is a basic CloudFormation stack that will deploy a lambda to handle SNS published messages and then send them to your nomiated Slack channel for notification.

The stack will securely store your Slack Webhook URL in AWS Secrets Manager

## Use case

Standard use case for this CloudFormation stack is quite broad, you can essentially publish any type of data to the SNS topic and the lambda function will handle the SNS payload and use the `Message` key value and send it on to your Slack channel.

The SNS message can be anything you like, you could expand the lambda function to handle certain subjects differently if desired.

## AWS Services used

- AWS CloudFormation
- AWS Lambda
- AWS Secret Manager
- AWS Simple Notification Service

## Prerquisites

- AWS Account access with the above AWS service permissions
- AWS CLI
- An S3 bucket where your deployment can be published


## Deployment

Note: You must ensure the bash script is executable prior to running the following steps. You can do this by opening a terminal window, navigating to the root of the repository and running the following command `chmod +x deploy.sh`

### Required Values

- **ARTIFACT_BUCKET** - This is the NAME of the AWS S3 bucket where your package will be published to for using during deployment
- **CFN_STACK_NAME** - The name you wish to give the CloudFormation stack.
    - Note: Some resources created use the stack name as a naming prefix
- **SLACK_CHANNEL** - This is the Slack channel you want the notifications to go to
- **SLACK_WEBHOOK_URL** - The full URL Slack provided you after creating your webhook

### Steps

- Run the following command to deploy the CloudFormation stack
- Note: Ensure you replace the place holder values with your data
- `./deploy.sh <ARTIFACT_BUCKET> <CFN_STACK_NAME> <SLACK_CHANNEL>'<SLACK_WEBHOOK_URL>'`
    - Example - `./deploy.sh my-artifact-bucket aws-slack-notifier aws-notification-demo 'https://slack.com/webhookurl'`
- This should deploy the stack without issue

## Known shortfalls

- The solution is deliberately not over engineered, it's more to provide a quick solution and easy to understand approach to write something similar or improve upon it
- The AWS SDK provided `requests` module is depreciated and will be removed 31/3/2020 and will break this solution
    - The suggested fix is to either package the `requests` module with this solution or;
    - Investigate adding the AWS Python SDK Lambda Layer
- Futher customisation is definitely possible using this solution, it was kept simple on purpose
- Calling AWS Secrets Manager for every message may prove troublesome and has not been performance tested
- You could take a heavy encryption route with the Webhook URL if desired, again, avoidance of over engineering was taken
- Updating this stack will require **ALL* the parameters to be passed again regardless of change, this could be improvement upon if desired


## Licensing and Usage

- This repository is covered by an MIT license, and it's usage must align to this license

## Feedback

Welcome to take any feedback, PRs or issue requests, this was just an afternoon project.
