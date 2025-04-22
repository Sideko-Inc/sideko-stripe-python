import pydantic
import typing
import typing_extensions


class AccountCreateBodyCapabilitiesRevolutPayPayments(typing_extensions.TypedDict):
    """
    AccountCreateBodyCapabilitiesRevolutPayPayments
    """

    requested: typing_extensions.NotRequired[bool]


class _SerializerAccountCreateBodyCapabilitiesRevolutPayPayments(pydantic.BaseModel):
    """
    Serializer for AccountCreateBodyCapabilitiesRevolutPayPayments handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    requested: typing.Optional[bool] = pydantic.Field(alias="requested", default=None)
