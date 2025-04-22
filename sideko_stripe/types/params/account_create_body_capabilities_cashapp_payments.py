import pydantic
import typing
import typing_extensions


class AccountCreateBodyCapabilitiesCashappPayments(typing_extensions.TypedDict):
    """
    AccountCreateBodyCapabilitiesCashappPayments
    """

    requested: typing_extensions.NotRequired[bool]


class _SerializerAccountCreateBodyCapabilitiesCashappPayments(pydantic.BaseModel):
    """
    Serializer for AccountCreateBodyCapabilitiesCashappPayments handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    requested: typing.Optional[bool] = pydantic.Field(alias="requested", default=None)
