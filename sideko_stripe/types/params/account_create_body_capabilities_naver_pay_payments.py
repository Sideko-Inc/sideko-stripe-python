import pydantic
import typing
import typing_extensions


class AccountCreateBodyCapabilitiesNaverPayPayments(typing_extensions.TypedDict):
    """
    AccountCreateBodyCapabilitiesNaverPayPayments
    """

    requested: typing_extensions.NotRequired[bool]


class _SerializerAccountCreateBodyCapabilitiesNaverPayPayments(pydantic.BaseModel):
    """
    Serializer for AccountCreateBodyCapabilitiesNaverPayPayments handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    requested: typing.Optional[bool] = pydantic.Field(alias="requested", default=None)
