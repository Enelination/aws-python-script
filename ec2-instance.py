import boto3

# Create an EC2 client
ec2 = boto3.client('ec2')

# Define the parameters for the EC2 instance
params = {
    'ImageId': 'ami-0ff8a91507f77f867',  # Ubuntu 18.04 LTS
    'InstanceType': 't2.micro',
    'MinCount': 1,
    'MaxCount': 1
}

# Launch the EC2 instance
response = ec2.run_instances(**params)
print(response)
