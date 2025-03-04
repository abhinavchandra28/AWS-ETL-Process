# AWS-ETL-Process
End to end AWS based ETL Process using - S3, Glue and Lambda Functions


This repository contains an end-to-end batch ETL pipeline using AWS services to process and store data.

📌 Pipeline Workflow

1️⃣ Raw Data Storage → Upload raw CSV files to S3

2️⃣ ETL Processing → AWS Glue extracts, transforms & loads data

3️⃣ Data Storage → Amazon Redshift stores transformed data

4️⃣ Automation → AWS Lambda triggers Glue when new files are uploaded

5️⃣ Deployment → Use Python Boto3 to deploy the infrastructure
