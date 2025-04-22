import pydantic
import typing
import typing_extensions


class AccountUpdateBodyCapabilitiesRevolutPayPayments(typing_extensions.TypedDict):
    """
    AccountUpdateBodyCapabilitiesRevolutPayPayments
    """

    requested: typing_extensions.NotRequired[bool]


class _SerializerAccountUpdateBodyCapabilitiesRevolutPayPayments(pydantic.BaseModel):
    """
    Serializer for AccountUpdateBodyCapabilitiesRevolutPayPayments handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    requested: typing.Optional[bool] = pydantic.Field(alias="requested", default=None)
