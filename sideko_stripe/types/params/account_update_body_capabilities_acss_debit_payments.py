import pydantic
import typing
import typing_extensions


class AccountUpdateBodyCapabilitiesAcssDebitPayments(typing_extensions.TypedDict):
    """
    AccountUpdateBodyCapabilitiesAcssDebitPayments
    """

    requested: typing_extensions.NotRequired[bool]


class _SerializerAccountUpdateBodyCapabilitiesAcssDebitPayments(pydantic.BaseModel):
    """
    Serializer for AccountUpdateBodyCapabilitiesAcssDebitPayments handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    requested: typing.Optional[bool] = pydantic.Field(alias="requested", default=None)
