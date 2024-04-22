# Toman escrow account OAuth 2.0 and API Usage Guide

This guide provides instructions for interacting marketplaces with Toman escrow account OAuth 2.0 service to obtain access tokens, and then utilizing the obtained JWT token to access the main service APIs.

* [Toman Escrow Account Service OpenAPI Specification](https://docs.tomanpay.net/swagger/b2c.html)


## Step 1: Working with OAuth 2.0 Service

### Obtaining Access Token
To obtain an access token from the OAuth 2.0 service, follow these steps:

    Note: In the initial step, ensure you possess a valid `client_id` and `client_secret`. For further details, please reach out to our team.

1 - Authentication: Authenticate your client application and obtain access token with the OAuth 2.0 service using the appropriate credentials (`client_id` and `client_secret`).

    Note: deal:write scope is required for deal creation flow.

```shell
curl --location 'https://accounts.tomanpay.net/realms/toman/protocol/openid-connect/token' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'grant_type=client_credentials' \
--data-urlencode 'client_id=<your_client_id>' \
--data-urlencode 'client_secret=<your_client_secret>'
--data-urlencode 'scope=deal:write'
```

### Refreshing Access Token
If the access token expires or becomes invalid, you can refresh it using a refresh token. Here's how:

Token Refresh Request: Send a token refresh request to the OAuth 2.0 service, providing the `refresh_token` and client credentials with desired refresh_token grant type.

Token Refresh Response: Receive a new access token and, optionally, a new refresh token in the response.

```shell
curl --location 'https://accounts.tomanpay.net/realms/toman/protocol/openid-connect/token' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'grant_type=refresh_token' \
--data-urlencode 'client_id=<your_client_id>' \
--data-urlencode 'client_secret=<your_client_secrete>' \
--data-urlencode 'refresh_token=<obtained_refresh_token>'
```

## Step 2: Working with Main Service APIs
After obtaining a valid JWT token from the OAuth 2.0 service, you can use it to access the main service APIs. Follow these steps:

1 - Create a deal using the following payload structure, and upon completion, redirect the current user to the specified `redirect_url` in response.

### Create Deal:
    Note: deal:create scope is required for this resource.
#### POST /escrow/api/v1/providers/{provider_slug}/payees/{payee_slug}/deals

- **Security**: OAuth2 (Scope: deal:write)
- **Description**: Create a specific deal
- **Parameters**:
  - `provider_slug` (path): Unique provider's slug
- **Request Body**: DealCreationRequestDTO
- **Responses**:
  - `201`: Created (DealCreationResponseDTO)
  - `401`: Authentication failed


```shell
curl --location 'https://api.tomanpay.net/escrow/api/v1/providers/{provider_slug}/payees/{payee_slug}/deals' \
--header 'Authorization: Bearer <OBTAINED_ACCESS_TOKEN>' \
--header 'Content-Type: application/json' \
--data '{
  "res_number":"123123123",
  "redirect_url":"https://<YOUR_DOMAIN>/<ENDPOINT_TO_CALL_AFTER_PAYMENT>",
  "category":"Goods",
  "items":[
    {
      "name": "string",
      "price": 80000,
      "quantity": 1,
      "description": "توضیحات",
      "image_urls": [
        "https://en.wikipedia.org/wiki/Cicada_3301",
        "https://en.wikipedia.org/wiki/Pokémon"
      ]
    }
  ]
}'
```

2 - After redirecting the user to the specified `redirect_url`, we escort him/her to the payment gateway. Upon successful payment, we redirect the payer back to the predefined `redirect_url`  set during the deal creation process and notify your service of the payment result.

    Note: payment's result info contains res_number, trace_number and payment_result as success or fail.

## Additional Notes

Ensure that you securely store and manage access tokens and refresh tokens to prevent unauthorized access to resources.


### <em>If you have any additional questions, please don't hesitate to contact us. Furthermore, if you have any suggestions to enhance this documentation, we welcome your feedback.</em>
