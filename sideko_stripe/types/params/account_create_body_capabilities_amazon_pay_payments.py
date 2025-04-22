import pydantic
import typing
import typing_extensions


class AccountCreateBodyCapabilitiesAmazonPayPayments(typing_extensions.TypedDict):
    """
    AccountCreateBodyCapabilitiesAmazonPayPayments
    """

    requested: typing_extensions.NotRequired[bool]


class _SerializerAccountCreateBodyCapabilitiesAmazonPayPayments(pydantic.BaseModel):
    """
    Serializer for AccountCreateBodyCapabilitiesAmazonPayPayments handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    requested: typing.Optional[bool] = pydantic.Field(alias="requested", default=None)
