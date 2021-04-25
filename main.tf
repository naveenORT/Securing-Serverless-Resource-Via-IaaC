provider "aws" {
  profile = "root"
  region  = "us-east-1"
}

resource "aws_lambda_function" "info7150lambda" {
  function_name = "info7150lambda"
  filename      =  data.archive_file.helloworld.output_path
  role          =  aws_iam_role.LambdaServiceRole.arn
  handler       = "index.handler"
  runtime       = "python3.7"
}

data "archive_file" "helloworld" {
  type        = "zip"
  output_path = "payload.zip"
  source {
    filename = "lambdascript.py"
    content = "//"
  }
}

resource "aws_iam_role" "LambdaServiceRole" {
  name = "LambdaServiceRole"
  assume_role_policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": "sts:AssumeRole",
      "Principal": {
        "Service": "lambda.amazonaws.com"
      },
      "Effect": "Allow",
      "Sid": ""
    }
  ]
}
EOF
}

resource "aws_iam_user_policy" "GH-Update-Lambda" {
  name = "GH-Update-Lambda"
  user = "User-1"

  policy = <<-EOF
  {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action": [
                "lambda:InvokeFunction", 
                "lambda:UpdateFunctionCode",
                "lambda:GetFunction",
                "lambda:CreateFunction",
                "lambda:DeleteFunction"
            ],
            "Resource": "arn:aws:lambda:*:315895091735:function:*"
        },
        {
            "Sid": "VisualEditor1",
            "Effect": "Allow",
            "Action": "lambda:ListFunctions",
            "Resource": "*"
        }
    ]
  }
  EOF
}

resource "aws_iam_user_policy_attachment" "LambdaFullAccess" {
  user       = data.aws_iam_user.user1.user_name
  policy_arn = "arn:aws:iam::aws:policy/AWSLambda_FullAccess"
}

data "aws_iam_user" "user1" {
  user_name = "User-1"
}
