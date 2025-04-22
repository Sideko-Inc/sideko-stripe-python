import pydantic
import typing
import typing_extensions


class AccountUpdateBodyCapabilitiesMultibancoPayments(typing_extensions.TypedDict):
    """
    AccountUpdateBodyCapabilitiesMultibancoPayments
    """

    requested: typing_extensions.NotRequired[bool]


class _SerializerAccountUpdateBodyCapabilitiesMultibancoPayments(pydantic.BaseModel):
    """
    Serializer for AccountUpdateBodyCapabilitiesMultibancoPayments handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    requested: typing.Optional[bool] = pydantic.Field(alias="requested", default=None)
