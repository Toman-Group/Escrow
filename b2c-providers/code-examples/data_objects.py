from dataclasses import dataclass
from typing import Optional

from constants import GrantTypeEnum, ProviderInfo


@dataclass
class AccessTokenErrorResponseDTO:
    grant_type: GrantTypeEnum
    client_id: str = ProviderInfo.ClientID
    client_secret: str = ProviderInfo.ClientSecret
    refresh_token: Optional[str] = None


@dataclass
class AccessTokenResponseDTO:
    access_token: str
    expires_in: int
    refresh_expires_in: int
    token_type: str
    not_before_policy: int
    scope: str


@dataclass
class AccessTokenErrorResponseDTO:
    error: str
    error_description: str
