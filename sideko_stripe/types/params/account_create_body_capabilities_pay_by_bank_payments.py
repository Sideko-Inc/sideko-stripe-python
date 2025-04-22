import pydantic
import typing
import typing_extensions


class AccountCreateBodyCapabilitiesPayByBankPayments(typing_extensions.TypedDict):
    """
    AccountCreateBodyCapabilitiesPayByBankPayments
    """

    requested: typing_extensions.NotRequired[bool]


class _SerializerAccountCreateBodyCapabilitiesPayByBankPayments(pydantic.BaseModel):
    """
    Serializer for AccountCreateBodyCapabilitiesPayByBankPayments handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    requested: typing.Optional[bool] = pydantic.Field(alias="requested", default=None)
