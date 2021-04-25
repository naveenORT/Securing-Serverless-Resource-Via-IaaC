#!/bin/bash

#Python function to fetch terraform template from S3 Bucket

echo 'Executing python function to fetch terraform template from S3 Bucket'

python3 deploy-cli.py

terraform init

terraform apply -auto-approve

After installing prerequisites to deploy serverless resource (AWS Lambda) in a secure manner,

> Start bash script using this command
```sh
bash execute.sh 
```
