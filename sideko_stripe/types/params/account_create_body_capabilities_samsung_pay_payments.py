import pydantic
import typing
import typing_extensions


class AccountCreateBodyCapabilitiesSamsungPayPayments(typing_extensions.TypedDict):
    """
    AccountCreateBodyCapabilitiesSamsungPayPayments
    """

    requested: typing_extensions.NotRequired[bool]


class _SerializerAccountCreateBodyCapabilitiesSamsungPayPayments(pydantic.BaseModel):
    """
    Serializer for AccountCreateBodyCapabilitiesSamsungPayPayments handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    requested: typing.Optional[bool] = pydantic.Field(alias="requested", default=None)
