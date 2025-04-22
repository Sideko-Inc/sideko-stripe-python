import pydantic
import typing
import typing_extensions

from .account_person_create_body_additional_tos_acceptances_account import (
    AccountPersonCreateBodyAdditionalTosAcceptancesAccount,
    _SerializerAccountPersonCreateBodyAdditionalTosAcceptancesAccount,
)


class AccountPersonCreateBodyAdditionalTosAcceptances(typing_extensions.TypedDict):
    """
    Details on the legal guardian's or authorizer's acceptance of the required Stripe agreements.
    """

    account: typing_extensions.NotRequired[
        AccountPersonCreateBodyAdditionalTosAcceptancesAccount
    ]


class _SerializerAccountPersonCreateBodyAdditionalTosAcceptances(pydantic.BaseModel):
    """
    Serializer for AccountPersonCreateBodyAdditionalTosAcceptances handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    account: typing.Optional[
        _SerializerAccountPersonCreateBodyAdditionalTosAcceptancesAccount
    ] = pydantic.Field(alias="account", default=None)
