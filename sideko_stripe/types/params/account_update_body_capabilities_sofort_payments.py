import pydantic
import typing
import typing_extensions


class AccountUpdateBodyCapabilitiesSofortPayments(typing_extensions.TypedDict):
    """
    AccountUpdateBodyCapabilitiesSofortPayments
    """

    requested: typing_extensions.NotRequired[bool]


class _SerializerAccountUpdateBodyCapabilitiesSofortPayments(pydantic.BaseModel):
    """
    Serializer for AccountUpdateBodyCapabilitiesSofortPayments handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    requested: typing.Optional[bool] = pydantic.Field(alias="requested", default=None)
