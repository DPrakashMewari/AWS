# Library import
import boto3
import pandas as pd

# Connection
s3 = boto3.resource(
    service_name='s3',
    region_name='us-east-2',
    aws_access_key_id='',
    aws_secret_access_key=''
)

# To check all buckets is s3
#for bucket in s3.buckets.all():
#   print(bucket.name)

# Creating a dataframe /csv that will going to upload
demo = pd.DataFrame({'Ram':[1,2,3],'Krishna':['a','b','c']})
demo.to_csv("demo.csv")
print(demo)

#s3.Bucket('prakash-bucket1').upload_file(Filename='demo.csv',Key='demo.csv')
print("File upload successfully")


for obj in s3.Bucket('prakash-bucket1').objects.all():
    print(obj)

print(s3.Bucket("prakash-bucket1").Object('demo.csv').get())
# It give response in : Body tag

# load csv from our s3 bucket
obj = s3.Bucket("prakash-bucket1").Object('demo.csv').get()
df = pd.read_csv(obj['Body'],index_col=0)
print(df)

# Download file
s3.Bucket("prakash-bucket1").download_file(Key='demo.csv',Filename='demo1.csv')
# Reading our file
pd.read_csv('demo1.csv')