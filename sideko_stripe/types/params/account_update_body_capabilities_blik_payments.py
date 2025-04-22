import pydantic
import typing
import typing_extensions


class AccountUpdateBodyCapabilitiesBlikPayments(typing_extensions.TypedDict):
    """
    AccountUpdateBodyCapabilitiesBlikPayments
    """

    requested: typing_extensions.NotRequired[bool]


class _SerializerAccountUpdateBodyCapabilitiesBlikPayments(pydantic.BaseModel):
    """
    Serializer for AccountUpdateBodyCapabilitiesBlikPayments handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    requested: typing.Optional[bool] = pydantic.Field(alias="requested", default=None)
