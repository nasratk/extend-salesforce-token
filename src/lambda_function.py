import os
import json
import requests

def lambda_handler(event, context):
    # Salesforce connected app credentials from environment variables
    client_id = os.getenv('SALESFORCE_CLIENT_ID')
    client_secret = os.getenv('SALESFORCE_CLIENT_SECRET')
    refresh_token = os.getenv('SALESFORCE_REFRESH_TOKEN')
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

if __name__ == '__main__':
    event = {}
    context = None
    lambda_handler(event, context)
