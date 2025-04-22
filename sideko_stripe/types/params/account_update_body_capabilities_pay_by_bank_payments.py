import pydantic
import typing
import typing_extensions


class AccountUpdateBodyCapabilitiesPayByBankPayments(typing_extensions.TypedDict):
    """
    AccountUpdateBodyCapabilitiesPayByBankPayments
    """

    requested: typing_extensions.NotRequired[bool]


class _SerializerAccountUpdateBodyCapabilitiesPayByBankPayments(pydantic.BaseModel):
    """
    Serializer for AccountUpdateBodyCapabilitiesPayByBankPayments handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    requested: typing.Optional[bool] = pydantic.Field(alias="requested", default=None)
