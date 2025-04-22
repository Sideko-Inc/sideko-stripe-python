import pydantic
import typing
import typing_extensions


class AccountUpdateBodyCapabilitiesCashappPayments(typing_extensions.TypedDict):
    """
    AccountUpdateBodyCapabilitiesCashappPayments
    """

    requested: typing_extensions.NotRequired[bool]


class _SerializerAccountUpdateBodyCapabilitiesCashappPayments(pydantic.BaseModel):
    """
    Serializer for AccountUpdateBodyCapabilitiesCashappPayments handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    requested: typing.Optional[bool] = pydantic.Field(alias="requested", default=None)
