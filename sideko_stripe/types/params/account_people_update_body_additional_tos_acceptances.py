import pydantic
import typing
import typing_extensions

from .account_people_update_body_additional_tos_acceptances_account import (
    AccountPeopleUpdateBodyAdditionalTosAcceptancesAccount,
    _SerializerAccountPeopleUpdateBodyAdditionalTosAcceptancesAccount,
)


class AccountPeopleUpdateBodyAdditionalTosAcceptances(typing_extensions.TypedDict):
    """
    Details on the legal guardian's or authorizer's acceptance of the required Stripe agreements.
    """

    account: typing_extensions.NotRequired[
        AccountPeopleUpdateBodyAdditionalTosAcceptancesAccount
    ]


class _SerializerAccountPeopleUpdateBodyAdditionalTosAcceptances(pydantic.BaseModel):
    """
    Serializer for AccountPeopleUpdateBodyAdditionalTosAcceptances handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    account: typing.Optional[
        _SerializerAccountPeopleUpdateBodyAdditionalTosAcceptancesAccount
    ] = pydantic.Field(alias="account", default=None)
