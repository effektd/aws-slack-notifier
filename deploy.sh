#/bin/bash

# Package SAM template
aws cloudformation package --template-file cfn/template.yml --s3-bucket $1 --output-template-file packaged.yml

# Deploy packaged SAM template
aws cloudformation deploy --template-file ./packaged.yml --stack-name $2 --capabilities CAPABILITY_IAM

# Clean packaged SAM template

rm ./packaged.yml