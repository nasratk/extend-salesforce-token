import json
import requests

def lambda_handler(event, context):
    # Salesforce connected app credentials
    client_id = '3MVG9ZL0ppGP5UrCrqMBpTcesgjRbfX5O_sKWN3j.I8cNX6D7FKGK1GLLPw3B6Ko79VIsjQWQvImmTJYIFY0h'
    client_secret = 'A8F439191EB1B9B744EFCE1254315D03748E9212EA3F008F1300358E1C3F48EB'
    refresh_token = '5Aep861TSESvWeug_zJrKwzDXPX1LO920DfhQdFVY0Jjh7aitJpPbBP4ntcR0sdghJV0bjT20qD_GGHcyIU_yQV'
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
