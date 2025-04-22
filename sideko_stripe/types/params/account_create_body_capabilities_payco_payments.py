import pydantic
import typing
import typing_extensions


class AccountCreateBodyCapabilitiesPaycoPayments(typing_extensions.TypedDict):
    """
    AccountCreateBodyCapabilitiesPaycoPayments
    """

    requested: typing_extensions.NotRequired[bool]


class _SerializerAccountCreateBodyCapabilitiesPaycoPayments(pydantic.BaseModel):
    """
    Serializer for AccountCreateBodyCapabilitiesPaycoPayments handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    requested: typing.Optional[bool] = pydantic.Field(alias="requested", default=None)
