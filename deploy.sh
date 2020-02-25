#/bin/bash

BUCKET=$1
STACK_NAME=$2
CHANNEL=$3
WEBHOOK_URL=$4

# Package SAM template
aws cloudformation package --template-file cfn/template.yml --s3-bucket $BUCKET --output-template-file packaged.yml

# Deploy packaged SAM template
aws cloudformation deploy --template-file ./packaged.yml --stack-name $STACK_NAME --parameter-overrides SlackChannel=$CHANNEL SlackWebhookUrl=$WEBHOOK_URL --capabilities CAPABILITY_IAM

# Clean packaged SAM template
rm ./packaged.yml