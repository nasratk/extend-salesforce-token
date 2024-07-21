# Salesforce Token Refresh Lambda Function

This repository contains an AWS Lambda function that refreshes Salesforce tokens. The function reads credentials from the AWS Systems Manager (SSM) Parameter Store and uses these credentials to request a new access token from Salesforce. The function is triggered automatically at a specified interval using Amazon EventBridge.

This repository also contains files to deploy the Lambda function using SAM. The SAM template is defined in template.yaml

## Overview

- **Language**: Python 3.12
- **AWS Services**: Lambda, SSM Parameter Store, EventBridge Rule
- **Deployment**: AWS Serverless Application Model (SAM)

## Pre-requisites

- **Connected App in Salesforce**: Make sure you have created a connected app in your Salesforce account and noted Customer Key and Customer Secret. These parameters are referred to as Client ID and Client Secret in this template.
- **Refresh Token**: Make sure you have generated a refresh token

## Functionality

The Lambda function performs the following steps:
1. Retrieves Salesforce credentials (client ID, client secret, refresh token) from SSM Parameter Store.
2. Uses the credentials to request a new access token from Salesforce.
3. Logs the new access token and instance URL.

## Architecture

The following resources are deployed:
- **Lambda Function**: Handles the token refresh logic.
- **SSM Parameter Store**: Securely stores Salesforce credentials.
- **EventBridge Rule**: Triggers the Lambda function at a specified interval.

## SAM Template

The `template.yaml` file defines the AWS resources using the AWS SAM framework. The template includes:
- A Lambda function to refresh Salesforce tokens.
- SSM Parameters to store Salesforce credentials.
- An EventBridge rule to trigger the Lambda function at a specified interval.
- Required permissions for Lambda to access SSM Parameters and be invoked by EventBridge.

## Parameters

The template parameterises the interval between Lambda function invocations. You can specify the interval during deployment.

## Deployment

To deploy the application, use the AWS SAM CLI:

```bash
sam build
sam deploy --guided
```

During initial deployment, parameters are created using dummy values which you will need to be updated with the actual values for those parameters for the lambda function to operate.