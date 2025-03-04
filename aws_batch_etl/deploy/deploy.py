
import boto3
import json

s3_client = boto3.client('s3')
glue_client = boto3.client('glue')
redshift_client = boto3.client('redshift')
lambda_client = boto3.client('lambda')
iam_client = boto3.client('iam')

S3_BUCKET = "your-bucket-name"
GLUE_JOB_NAME = "batch-etl-job"
REDSHIFT_CLUSTER_ID = "data-warehouse"
LAMBDA_FUNCTION_NAME = "trigger-glue-job"
IAM_ROLE_NAME = "GlueLambdaExecutionRole"

def create_s3_bucket():
    s3_client.create_bucket(Bucket=S3_BUCKET)
    print(f"S3 bucket '{S3_BUCKET}' created.")

def create_glue_job():
    glue_client.create_job(
        Name=GLUE_JOB_NAME,
        RoleArn="arn:aws:iam::your-account-id:role/GlueRole",
        Command={"Name": "glueetl", "ScriptLocation": f"s3://{S3_BUCKET}/scripts/etl_script.py"},
        GlueVersion="3.0"
    )
    print(f"Glue job '{GLUE_JOB_NAME}' created.")

def create_redshift_cluster():
    redshift_client.create_cluster(
        ClusterIdentifier=REDSHIFT_CLUSTER_ID,
        NodeType="dc2.large",
        MasterUsername="your_user",
        MasterUserPassword="your_password",
        DBName="yourdbname",
        ClusterType="single-node"
    )
    print(f"Redshift cluster '{REDSHIFT_CLUSTER_ID}' created.")

def deploy():
    create_s3_bucket()
    create_glue_job()
    create_redshift_cluster()
    print("AWS Batch ETL Pipeline deployed!")

if __name__ == "__main__":
    deploy()
