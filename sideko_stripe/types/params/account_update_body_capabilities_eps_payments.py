import pydantic
import typing
import typing_extensions


class AccountUpdateBodyCapabilitiesEpsPayments(typing_extensions.TypedDict):
    """
    AccountUpdateBodyCapabilitiesEpsPayments
    """

    requested: typing_extensions.NotRequired[bool]


class _SerializerAccountUpdateBodyCapabilitiesEpsPayments(pydantic.BaseModel):
    """
    Serializer for AccountUpdateBodyCapabilitiesEpsPayments handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    requested: typing.Optional[bool] = pydantic.Field(alias="requested", default=None)
