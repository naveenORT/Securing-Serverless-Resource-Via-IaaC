import boto3
from prompt_toolkit import prompt
import os

# Enter Bucket Name
bucket_name = 'iaac.template.bucket'

# ToDos: Add color options to beautify CLI and outputs

if __name__ == '__main__':

    # Ask for user's access & secret access keys
    print('Auto Deployment - Enter your AWS Account Access & Secret access keys')
    access_keys = prompt('Enter your access key: ')
    secret_access_keys = prompt('Enter your secret access key: ')

    # Set Global CLI config
    try:
        os.system('aws configure set aws_access_key_id %s' % access_keys)
        os.system('aws configure set aws_secret_access_key  %s' % secret_access_keys)
    except Exception as e:
        print('Something went wrong. Error Details: %s' % e)

    print('AWS Configuration Set!')

    # UserID corresponds to the dir name in the given S3 bucket
    # All files for a given userID are stored in the respective directory
    user_id = prompt('Enter your User ID: ')
    print('Listing available Deployments for %s :' % user_id)

    # Connect to S3
    try:
        s3 = boto3.resource('s3')
        my_bucket = s3.Bucket(bucket_name)
    except Exception as e:
        print('Could not connect to S3')

    dir_contents = []
    num = 0

    # Print contents of the Bucket with the given prefix
    # Outputs contents that looks like this
    # 1 auto - deploy / user1 / test1.txt
    # 2 auto - deploy / user1 / test2.txt

    for object_summary in my_bucket.objects.filter(Prefix="auto-deploy/" + user_id + '/'):
        dir_contents.append(object_summary.key)
        print('%s %s' % (num, object_summary.key))
        num = num + 1

    # Choose a number to download the template and have it ready for terraform
    choice = prompt('Make a selection. Hint: Choose the number to be deployed: ')

    # Download the file as demo.txt - this can be replaced with the filename or can be kept static
    # to allow only one copy of the template/code to reside locally
    my_bucket.download_file(dir_contents[int(choice)], 'main.tf')
    my_bucket.download_file(dir_contents[int(choice)], 'vars.tf')
    
    print('Config Downloaded!')

    # Add Terraform commands here in os.system to allow execution of bash commands
    # os.system('echo hello')