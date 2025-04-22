import pydantic
import typing
import typing_extensions

from .token_create_body_person_additional_tos_acceptances_account import (
    TokenCreateBodyPersonAdditionalTosAcceptancesAccount,
    _SerializerTokenCreateBodyPersonAdditionalTosAcceptancesAccount,
)


class TokenCreateBodyPersonAdditionalTosAcceptances(typing_extensions.TypedDict):
    """
    TokenCreateBodyPersonAdditionalTosAcceptances
    """

    account: typing_extensions.NotRequired[
        TokenCreateBodyPersonAdditionalTosAcceptancesAccount
    ]


class _SerializerTokenCreateBodyPersonAdditionalTosAcceptances(pydantic.BaseModel):
    """
    Serializer for TokenCreateBodyPersonAdditionalTosAcceptances handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    account: typing.Optional[
        _SerializerTokenCreateBodyPersonAdditionalTosAcceptancesAccount
    ] = pydantic.Field(alias="account", default=None)
