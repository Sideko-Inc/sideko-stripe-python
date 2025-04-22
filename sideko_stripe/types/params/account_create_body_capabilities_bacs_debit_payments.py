import pydantic
import typing
import typing_extensions


class AccountCreateBodyCapabilitiesBacsDebitPayments(typing_extensions.TypedDict):
    """
    AccountCreateBodyCapabilitiesBacsDebitPayments
    """

    requested: typing_extensions.NotRequired[bool]


class _SerializerAccountCreateBodyCapabilitiesBacsDebitPayments(pydantic.BaseModel):
    """
    Serializer for AccountCreateBodyCapabilitiesBacsDebitPayments handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    requested: typing.Optional[bool] = pydantic.Field(alias="requested", default=None)
