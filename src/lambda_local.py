import requests

def lambda_handler(event, context=None):
    client_id = 'YOUR_CLIENT_ID'
    client_secret = 'YOUR_CLIENT_SECRET'
    refresh_token = 'YOUR_REFRESH_TOKEN'
    token_url = 'https://login.salesforce.com/services/oauth2/token'

    payload = {
        'grant_type': 'refresh_token',
        'client_id': client_id,
        'client_secret': client_secret,
        'refresh_token': refresh_token
    }

    response = requests.post(token_url, data=payload)
    response_json = response.json()

    if response.status_code == 200:
        print("Token refreshed successfully!")
    else:
        print(f"Failed to refresh token: {response_json}")

if __name__ == '__main__':
    event = {}
    context = None
    lambda_handler(event, context)
