import json
import boto3
import requests

# Initialize AWS SDK clients
ssm_client = boto3.client('ssm')

# Function to retrieve parameter from Parameter Store
def get_parameter(name):
    response = ssm_client.get_parameter(Name=name, WithDecryption=True)
    return response['Parameter']['Value']

def lambda_handler(event, context):
    # Retrieve Salesforce credentials from Parameter Store
    client_id = get_parameter('/SalesforceClientId')
    client_secret = get_parameter('/SalesforceClientSecret')
    refresh_token = get_parameter('/SalesforceRefreshToken')
    token_url = 'https://login.salesforce.com/services/oauth2/token'

    # Request payload for token refresh
    payload = {
        'grant_type': 'refresh_token',
        'client_id': client_id,
        'client_secret': client_secret,
        'refresh_token': refresh_token
    }

    # Make a POST request to refresh the token
    response = requests.post(token_url, data=payload)
    response_json = response.json()

    if response.status_code == 200:
        access_token = response_json['access_token']
        instance_url = response_json['instance_url']

        print(f"Access Token: {access_token}")
        print(f"Instance URL: {instance_url}")

        return {
            'statusCode': 200,
            'body': json.dumps('Token refreshed successfully!')
        }
    else:
        print(f"Failed to refresh token: {response_json}")
        return {
            'statusCode': response.status_code,
            'body': json.dumps('Failed to refresh token.')
        }

# For local testing, simulate event and context
if __name__ == '__main__':
    event = {}
    context = None
    lambda_handler(event, context)
