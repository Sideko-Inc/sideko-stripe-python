import pydantic
import typing
import typing_extensions


class AccountCreateBodyCapabilitiesCartesBancairesPayments(typing_extensions.TypedDict):
    """
    AccountCreateBodyCapabilitiesCartesBancairesPayments
    """

    requested: typing_extensions.NotRequired[bool]


class _SerializerAccountCreateBodyCapabilitiesCartesBancairesPayments(
    pydantic.BaseModel
):
    """
    Serializer for AccountCreateBodyCapabilitiesCartesBancairesPayments handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    requested: typing.Optional[bool] = pydantic.Field(alias="requested", default=None)
