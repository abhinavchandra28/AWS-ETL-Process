import boto3

glue_client = boto3.client("glue")

def lambda_handler(event, context):
    response = glue_client.start_job_run(JobName="batch-etl-job")
    print(f"Triggered Glue Job: {response}")
