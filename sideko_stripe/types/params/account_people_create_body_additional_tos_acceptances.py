import pydantic
import typing
import typing_extensions

from .account_people_create_body_additional_tos_acceptances_account import (
    AccountPeopleCreateBodyAdditionalTosAcceptancesAccount,
    _SerializerAccountPeopleCreateBodyAdditionalTosAcceptancesAccount,
)


class AccountPeopleCreateBodyAdditionalTosAcceptances(typing_extensions.TypedDict):
    """
    Details on the legal guardian's or authorizer's acceptance of the required Stripe agreements.
    """

    account: typing_extensions.NotRequired[
        AccountPeopleCreateBodyAdditionalTosAcceptancesAccount
    ]


class _SerializerAccountPeopleCreateBodyAdditionalTosAcceptances(pydantic.BaseModel):
    """
    Serializer for AccountPeopleCreateBodyAdditionalTosAcceptances handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    account: typing.Optional[
        _SerializerAccountPeopleCreateBodyAdditionalTosAcceptancesAccount
    ] = pydantic.Field(alias="account", default=None)
