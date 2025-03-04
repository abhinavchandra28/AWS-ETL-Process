from awsglue.context import GlueContext
from pyspark.context import SparkContext
from awsglue.dynamicframe import DynamicFrame
from awsglue.utils import getResolvedOptions

# Initialize Spark & Glue context
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session

# Load data from S3
s3_input_path = "s3://your-bucket-name/raw-data/sample.csv"
dynamic_frame = glueContext.create_dynamic_frame.from_options(
    connection_type="s3",
    connection_options={"paths": [s3_input_path]},
    format="csv",
    format_options={"withHeader": True}
)

# Transform data
df = dynamic_frame.toDF()
df_transformed = df.filter(df["column_name"].isNotNull())

# Save to Redshift
glueContext.write_dynamic_frame.from_options(
    frame=DynamicFrame.fromDF(df_transformed, glueContext),
    connection_type="redshift",
    connection_options={"url": "jdbc:redshift://your-redshift-cluster:5439/yourdbname",
                        "dbtable": "public.processed_data",
                        "user": "your_user",
                        "password": "your_password",
                        "redshiftTmpDir": "s3://your-bucket-name/temp/"},
)
print("ETL Completed!")

