import pydantic
import typing
import typing_extensions


class AccountCreateBodyCapabilitiesAcssDebitPayments(typing_extensions.TypedDict):
    """
    AccountCreateBodyCapabilitiesAcssDebitPayments
    """

    requested: typing_extensions.NotRequired[bool]


class _SerializerAccountCreateBodyCapabilitiesAcssDebitPayments(pydantic.BaseModel):
    """
    Serializer for AccountCreateBodyCapabilitiesAcssDebitPayments handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    requested: typing.Optional[bool] = pydantic.Field(alias="requested", default=None)
