import pydantic
import typing
import typing_extensions


class AccountUpdateBodyCapabilitiesBacsDebitPayments(typing_extensions.TypedDict):
    """
    AccountUpdateBodyCapabilitiesBacsDebitPayments
    """

    requested: typing_extensions.NotRequired[bool]


class _SerializerAccountUpdateBodyCapabilitiesBacsDebitPayments(pydantic.BaseModel):
    """
    Serializer for AccountUpdateBodyCapabilitiesBacsDebitPayments handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    requested: typing.Optional[bool] = pydantic.Field(alias="requested", default=None)
