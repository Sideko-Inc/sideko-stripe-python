import pydantic
import typing
import typing_extensions


class AccountUpdateBodyCapabilitiesAmazonPayPayments(typing_extensions.TypedDict):
    """
    AccountUpdateBodyCapabilitiesAmazonPayPayments
    """

    requested: typing_extensions.NotRequired[bool]


class _SerializerAccountUpdateBodyCapabilitiesAmazonPayPayments(pydantic.BaseModel):
    """
    Serializer for AccountUpdateBodyCapabilitiesAmazonPayPayments handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    requested: typing.Optional[bool] = pydantic.Field(alias="requested", default=None)
