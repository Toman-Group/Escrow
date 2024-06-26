# Escrow API Usage Guide - B2C Platforms

This guide provides instructions on how to integrate the Toman Escrow service into your B2C platform. For further details, you can refer to our [API documentation](https://docs.tomanpay.net/swagger/b2c.html).

**Note**: Ensure you have a valid `client_id`, `client_secret`, and `app_slug`. For further details, please contact our team.

## Table of Contents

- [Flow of a Deal in Escrow](#flow-of-a-deal-in-escrow)
- [Obtaining an Access Token](#obtaining-an-access-token)
- [Refreshing an Access Token](#refreshing-an-access-token)
- [Detail of Provider](#detail-of-provider)
- [Creation of Business](#creation-of-business)
- [Creation of Deal](#creation-of-deal)
- [Detail of Deal](#detail-of-deal)
- [Verify the Deal](#verify-the-deal)
- [Change State of Deal](#change-state-of-deal)
- [Additional Notes](#additional-notes)
- [Test Environment](#test-environment)
- [API Usage Flow](#api-usage-flow)
- [Contact Us](#contact-us)

## Flow of a Deal in Escrow

![Purchase drawio](https://github.com/Toman-Group/Escrow/assets/15687474/2770096c-f87e-4d1c-9a14-679646f09553)

## Obtaining an Access Token

Authenticate your client application and obtain an access token from the OAuth 2.0 service using your credentials (`client_id` and `client_secret`).

[Refer to Swagger](https://docs.tomanpay.net/swagger/b2c.html#/Authentication/post_realms__realm__protocol_openid_connect_token)

**Note**: Use `client_credentials` as the `grant_type` of the request.

After obtaining a valid JWT token from the OAuth 2.0 service, you can use it to access the main service APIs.

## Refreshing an Access Token

If the access token expires or becomes invalid, you can refresh it using a refresh token.

[Refer to Swagger](https://docs.tomanpay.net/swagger/b2c.html#/Authentication/post_realms__realm__protocol_openid_connect_token)

**Note**: Use `refresh_token` as the `grant_type` of the request.

## Detail of Provider

This endpoint will return the data that was provided to us.

[Refer to Swagger](https://docs.tomanpay.net/swagger/b2c.html#/Provider/get_escrow_api_v2_providers_me)

## Creation of Business

With this endpoint, you can add a shop/business that you want to activate Escrow for.

[Refer to Swagger](https://docs.tomanpay.net/swagger/b2c.html#/Business/post_escrow_api_v2_providers__provider_slug__businesses)

## Creation of Deal

You can create a deal using the access token with the documents in the following link. Upon completion, redirect the current user to the specified `redirect_url` in the response.

[Refer to Swagger](https://docs.tomanpay.net/swagger/b2c.html#/Deal/post_escrow_api_v2_providers__provider_slug__businesses__business_slug__deals)

After redirecting the user to the specified `redirect_url`, we escort the payer to the payment gateway. Upon successful payment, we redirect the payer back to the predefined `redirect_url` set during the deal creation process and notify your service of the payment result.

## Detail of Deal

You can check the `state` and `sub_state` of the deal at any time with the following endpoint.

[Refer to Swagger](https://docs.tomanpay.net/swagger/b2c.html#/Deal/get_escrow_api_v2_providers__provider_slug__deals__trace_number_)

## Verify the Deal

One of our settings allows you to either manually verify the created deal or let us assume it is verified. If you choose to manually verify the deal, its status after payment will be "Funded, New," and you have 12 hours to call the following endpoint. If we assume the deal is verified, after successful payment, the payer will land on Escrow, and the deal will be moved to "Funded, Init."

[Refer to Swagger](https://docs.tomanpay.net/swagger/b2c.html#/Deal/patch_escrow_api_v2_providers__provider_slug__deals__trace_number__verify_)

## Change State of Deal

You can move the deal forward with one of the following actions:
- `accept`: This action moves the deal forward and acts like the seller accepted their part of the deal.
- `ship`: This action moves the deal forward and moves the deal to the shipment state.

[Refer to Swagger](https://docs.tomanpay.net/swagger/b2c.html#/Deal/patch_escrow_api_v2_providers__provider_slug__deals__trace_number_)

## Additional Notes

- Ensure that you securely store and manage access tokens and refresh tokens to prevent unauthorized access to resources.
- To redirect the seller of the deal to the Toman WebApp, you can use the following template to create a URL: `<ENVIRONMENT_BASE_URL>/basket/{trace_number}`.

## Test Environment

To start testing APIs in a non-production environment, use the following base URLs:

**OAuth 2.0 Requests Base URL:**
- Staging: `https://keycloak-staging.qcluster.org`
- Production: `https://accounts.tomanpay.net`

**Escrow API Base URL:**
- Staging: `https://escrow-api-staging.qcluster.org`
- Production: `https://api.tomanpay.net`

**Escrow WebApp Base URL:**
- Staging: `https://escrow-staging-webapp.qcluster.org`
- Production: `https://escrow.tomanpay.net`

## API Usage Flow

1. **Obtaining an Access Token**:
   - First, get an access token by calling the OAuth 2.0 service using your `client_id` and `client_secret`.

2. **Refreshing an Access Token**:
   - If the access token expires, refresh it using a refresh token. You can know the expiration time from the `expires_in` field returned in the access token response.

3. **Validating the Access Token**:
   - To ensure your token is valid, call the `Detail of Provider` endpoint.

4. **Creating a Business**:
   - If you need to create a new business, call the `Creation of Business` endpoint. If the business is already created, this step can be skipped.

5. **Creating a Deal**:
   - Create a deal by calling the `Creation of Deal` endpoint. Redirect the user to the specified `redirect_url` in the response.

6. **Getting Deal Details**:
   - For information about the created deal or any previous deals, call the `Detail of Deal` endpoint using the `trace_number`.

7. **Verifying the Deal**:
   - If you opted to manually verify the deal, call the `Verify the Deal` endpoint within 12 hours after payment.

8. **Changing the State of the Deal**:
   - If you have opted for us to manage the state transitions:
     - Call the `Change State of Deal` endpoint with the action "accept" to set the payee for the deal.
     - Then call the endpoint again with the action "ship" to move the deal to "Funded, Sent".
   - If the deal price is fixed by you, the payee will be set during the deal creation.

## Contact Us

If you have any additional questions, please don't hesitate to contact us. We also welcome any suggestions to enhance this documentation.
