import boto3

# Create an Elastic Beanstalk client
eb = boto3.client('elasticbeanstalk')

# Define the parameters for the application
params = {
    'ApplicationName': 'my-app',
    'EnvironmentName': 'my-env',
    'SolutionStackName': '64bit Amazon Linux 2 v4.0.2 running Python 3.8'
}

# Create the Elastic Beanstalk environment
response = eb.create_environment(**params)
print(response)
