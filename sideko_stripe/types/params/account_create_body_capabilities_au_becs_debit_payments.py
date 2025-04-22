import pydantic
import typing
import typing_extensions


class AccountCreateBodyCapabilitiesAuBecsDebitPayments(typing_extensions.TypedDict):
    """
    AccountCreateBodyCapabilitiesAuBecsDebitPayments
    """

    requested: typing_extensions.NotRequired[bool]


class _SerializerAccountCreateBodyCapabilitiesAuBecsDebitPayments(pydantic.BaseModel):
    """
    Serializer for AccountCreateBodyCapabilitiesAuBecsDebitPayments handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    requested: typing.Optional[bool] = pydantic.Field(alias="requested", default=None)
