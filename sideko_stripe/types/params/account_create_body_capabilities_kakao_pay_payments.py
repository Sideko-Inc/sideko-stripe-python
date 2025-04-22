import pydantic
import typing
import typing_extensions


class AccountCreateBodyCapabilitiesKakaoPayPayments(typing_extensions.TypedDict):
    """
    AccountCreateBodyCapabilitiesKakaoPayPayments
    """

    requested: typing_extensions.NotRequired[bool]


class _SerializerAccountCreateBodyCapabilitiesKakaoPayPayments(pydantic.BaseModel):
    """
    Serializer for AccountCreateBodyCapabilitiesKakaoPayPayments handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    requested: typing.Optional[bool] = pydantic.Field(alias="requested", default=None)
