# Securing-Serverless-Resource-Via-IaaC

## Getting Started

### Install AWS CLI

Install the [AWS CLI on Linux]([https://docs.aws.amazon.com/cli/latest/userguide/install-linux.html)
and configure AWS CLI to your profile

### Install Terraform

Install the Terraform Using this command
```sh
apt install terraform 
```

### Python Dependencies for CLI

The CLI requires Python 3.7+ to run. Download and install Python from (here)[]

After installing prerequisites to deploy serverless resource (AWS Lambda) in a secure manner,


## Deploying Resources

Start bash script using this command
```sh
bash execute.sh 
```

This should start the CLI and you should be prompted for your details like `access_keys` and `secret_access_keys`. 
This requires all templates to be stored on S3 with the templates for a given user all grouped under the same directory.





