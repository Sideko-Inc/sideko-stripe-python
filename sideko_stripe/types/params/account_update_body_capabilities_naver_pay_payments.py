import pydantic
import typing
import typing_extensions


class AccountUpdateBodyCapabilitiesNaverPayPayments(typing_extensions.TypedDict):
    """
    AccountUpdateBodyCapabilitiesNaverPayPayments
    """

    requested: typing_extensions.NotRequired[bool]


class _SerializerAccountUpdateBodyCapabilitiesNaverPayPayments(pydantic.BaseModel):
    """
    Serializer for AccountUpdateBodyCapabilitiesNaverPayPayments handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    requested: typing.Optional[bool] = pydantic.Field(alias="requested", default=None)
