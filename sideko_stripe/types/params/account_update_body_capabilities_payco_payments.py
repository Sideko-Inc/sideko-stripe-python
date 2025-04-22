import pydantic
import typing
import typing_extensions


class AccountUpdateBodyCapabilitiesPaycoPayments(typing_extensions.TypedDict):
    """
    AccountUpdateBodyCapabilitiesPaycoPayments
    """

    requested: typing_extensions.NotRequired[bool]


class _SerializerAccountUpdateBodyCapabilitiesPaycoPayments(pydantic.BaseModel):
    """
    Serializer for AccountUpdateBodyCapabilitiesPaycoPayments handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    requested: typing.Optional[bool] = pydantic.Field(alias="requested", default=None)
