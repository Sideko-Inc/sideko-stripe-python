import pydantic
import typing
import typing_extensions


class AccountUpdateBodyCapabilitiesSamsungPayPayments(typing_extensions.TypedDict):
    """
    AccountUpdateBodyCapabilitiesSamsungPayPayments
    """

    requested: typing_extensions.NotRequired[bool]


class _SerializerAccountUpdateBodyCapabilitiesSamsungPayPayments(pydantic.BaseModel):
    """
    Serializer for AccountUpdateBodyCapabilitiesSamsungPayPayments handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    requested: typing.Optional[bool] = pydantic.Field(alias="requested", default=None)
