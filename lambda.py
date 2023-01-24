import boto3

# Create a Lambda client
lambda_client = boto3.client('lambda')

# Define the parameters for the Lambda function
params = {
    'FunctionName': 'my-function',
    'Runtime': 'python3.8',
    'Role': 'arn:aws:iam::1234567890:role/lambda_role',
    'Handler': 'main.handler',
    'Code': {
        'ZipFile': b'...'  # The code for the function in a zip file format
    }
}
response = lambda_client.create_function(**params)
print(response)
