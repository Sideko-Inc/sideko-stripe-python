import pydantic
import typing
import typing_extensions


class AccountUpdateBodyCapabilitiesCartesBancairesPayments(typing_extensions.TypedDict):
    """
    AccountUpdateBodyCapabilitiesCartesBancairesPayments
    """

    requested: typing_extensions.NotRequired[bool]


class _SerializerAccountUpdateBodyCapabilitiesCartesBancairesPayments(
    pydantic.BaseModel
):
    """
    Serializer for AccountUpdateBodyCapabilitiesCartesBancairesPayments handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    requested: typing.Optional[bool] = pydantic.Field(alias="requested", default=None)
