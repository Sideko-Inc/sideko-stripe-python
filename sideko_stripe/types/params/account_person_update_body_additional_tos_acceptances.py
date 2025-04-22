import pydantic
import typing
import typing_extensions

from .account_person_update_body_additional_tos_acceptances_account import (
    AccountPersonUpdateBodyAdditionalTosAcceptancesAccount,
    _SerializerAccountPersonUpdateBodyAdditionalTosAcceptancesAccount,
)


class AccountPersonUpdateBodyAdditionalTosAcceptances(typing_extensions.TypedDict):
    """
    Details on the legal guardian's or authorizer's acceptance of the required Stripe agreements.
    """

    account: typing_extensions.NotRequired[
        AccountPersonUpdateBodyAdditionalTosAcceptancesAccount
    ]


class _SerializerAccountPersonUpdateBodyAdditionalTosAcceptances(pydantic.BaseModel):
    """
    Serializer for AccountPersonUpdateBodyAdditionalTosAcceptances handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    account: typing.Optional[
        _SerializerAccountPersonUpdateBodyAdditionalTosAcceptancesAccount
    ] = pydantic.Field(alias="account", default=None)
