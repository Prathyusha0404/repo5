import boto3

# Replace these values with your AWS access key ID and secret access key
aws_access_key_id = 'YOUR_ACCESS_KEY_ID'
aws_secret_access_key = 'YOUR_SECRET_ACCESS_KEY'

# Replace this value with the ID of your EC2 instance
instance_id = 'YOUR_INSTANCE_ID'

# Create a new EC2 client
ec2 = boto3.client('ec2', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)

# Stop the EC2 instance
response = ec2.stop_instances(InstanceIds=[instance_id])

print(response)

