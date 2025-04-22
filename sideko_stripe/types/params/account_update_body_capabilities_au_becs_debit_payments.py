import pydantic
import typing
import typing_extensions


class AccountUpdateBodyCapabilitiesAuBecsDebitPayments(typing_extensions.TypedDict):
    """
    AccountUpdateBodyCapabilitiesAuBecsDebitPayments
    """

    requested: typing_extensions.NotRequired[bool]


class _SerializerAccountUpdateBodyCapabilitiesAuBecsDebitPayments(pydantic.BaseModel):
    """
    Serializer for AccountUpdateBodyCapabilitiesAuBecsDebitPayments handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    requested: typing.Optional[bool] = pydantic.Field(alias="requested", default=None)
