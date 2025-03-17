# AWS-ETL-Process
End to end AWS based ETL Process using - S3, Glue and Lambda Functions


This repository contains an end-to-end batch ETL pipeline using AWS services to process and store data.

📌 Pipeline Workflow

1️⃣ Raw Data Storage → Upload raw CSV files to S3

2️⃣ ETL Processing → AWS Glue extracts, transforms & loads data

3️⃣ Data Storage → Amazon Redshift stores transformed data

4️⃣ Automation → AWS Lambda triggers Glue when new files are uploaded

5️⃣ Deployment → Use Python Boto3 to deploy the infrastructure


Follow the following steps to set up your first etl on AWS:- 

1. Edit the glue_etl.py script according to your use case for the columns, data and tables in use.
2. Set up an AWS account with
  - Enabled S3, glue, lambda, step functions etc.
  - Create IAM roles.
  - Installed python 3.8+
  - Installed boto3 and CLI for deployment.
3. In the placeholder for S3 bucket, redshift username and password etc replace you paths/usernames/passwords.
