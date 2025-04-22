import pydantic
import typing
import typing_extensions


class AccountUpdateBodyCapabilitiesKakaoPayPayments(typing_extensions.TypedDict):
    """
    AccountUpdateBodyCapabilitiesKakaoPayPayments
    """

    requested: typing_extensions.NotRequired[bool]


class _SerializerAccountUpdateBodyCapabilitiesKakaoPayPayments(pydantic.BaseModel):
    """
    Serializer for AccountUpdateBodyCapabilitiesKakaoPayPayments handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    requested: typing.Optional[bool] = pydantic.Field(alias="requested", default=None)
