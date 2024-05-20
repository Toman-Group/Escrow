from dataclasses import asdict
from http import HTTPStatus
from typing import Optional, Union, Dict

import requests
from requests import Response

from constants import BaseURLs, ProviderInfo, GrantTypeEnum
from data_objects import AccessTokenResponseDTO, AccessTokenErrorResponseDTO

TOKEN_ENDPOINT = (
    BaseURLs.EscrowWebAppStaging
    + f"/realms/{ProviderInfo.Realm}/protocol/openid-connect/token"
)


def call_token_api(
    grant_type: GrantTypeEnum, refresh_token: Optional[str] = None
) -> Union[AccessTokenResponseDTO, AccessTokenErrorResponseDTO]:
    request_data: AccessTokenErrorResponseDTO = AccessTokenErrorResponseDTO(
        grant_type=grant_type, refresh_token=refresh_token
    )
    response: Response = requests.post(
        BaseURLs.EscrowWebAppStaging + "/realms/{realm}/protocol/openid-connect/token",
        data=asdict(request_data),
    )

    data: Dict = response.json()

    if response.status_code == HTTPStatus.OK:
        return AccessTokenResponseDTO(
            access_token=data["access_token"],
            expires_in=data["expires_in"],
            refresh_expires_in=data["refresh_expires_in"],
            token_type=data["token_type"],
            not_before_policy=data["not_before_policy"],
            scope=data["scope"],
        )

    return AccessTokenErrorResponseDTO(
        error=data["error"], error_description=data["error_description"]
    )
