import pydantic
import typing
import typing_extensions


class AccountCreateBodyCapabilitiesEpsPayments(typing_extensions.TypedDict):
    """
    AccountCreateBodyCapabilitiesEpsPayments
    """

    requested: typing_extensions.NotRequired[bool]


class _SerializerAccountCreateBodyCapabilitiesEpsPayments(pydantic.BaseModel):
    """
    Serializer for AccountCreateBodyCapabilitiesEpsPayments handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    requested: typing.Optional[bool] = pydantic.Field(alias="requested", default=None)
