import pydantic
import typing
import typing_extensions


class AccountCreateBodyCapabilitiesSofortPayments(typing_extensions.TypedDict):
    """
    AccountCreateBodyCapabilitiesSofortPayments
    """

    requested: typing_extensions.NotRequired[bool]


class _SerializerAccountCreateBodyCapabilitiesSofortPayments(pydantic.BaseModel):
    """
    Serializer for AccountCreateBodyCapabilitiesSofortPayments handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    requested: typing.Optional[bool] = pydantic.Field(alias="requested", default=None)
