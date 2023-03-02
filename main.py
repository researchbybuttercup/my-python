import boto3

# Replace with your access key and secret key
#AKIA5HBM57FZC5ZQRKFT
access_key = '<your-access-key>'
secret_key = '<your-secret-key>'

# Connect to EC2 using your access and secret key
ec2 = boto3.client('ec2', aws_access_key_id=access_key, aws_secret_access_key=secret_key)

# Get list of all EC2 instances
instances = ec2.describe_instances()

# Loop through the reservations and instances to print instance IDs
for reservation in instances['Reservations']:
    for instance in reservation['Instances']:
        print(instance['InstanceId'])


