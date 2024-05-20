import enum


class ProviderInfo:
    Name = "<YOUR_PROVIDER_NAME>"
    ClientID = "<YOUR_CLIENT_ID>"
    ClientSecret = "<YOUR_CLIENT_SECRET>"
    Realm = "toman"


class BaseURLs:
    OAuthStaging = "https://keycloak-staging.qcluster.org"
    OAuthProduction = "https://accounts.tomanpay.net"
    EscrowAPIStaging = "https://escrow-api-staging.qcluster.org"
    EscrowAPIProduction = "https://api.tomanpay.net"
    EscrowWebAppStaging = "https://escrow-staging-webapp.qcluster.org"
    EscrowWebAppProduction = "https://escrow.tomanpay.net"


class GrantTypeEnum(enum.Enum):
    ClientCredentials = "client_credentials"
    RefreshToken = "refresh_token"
