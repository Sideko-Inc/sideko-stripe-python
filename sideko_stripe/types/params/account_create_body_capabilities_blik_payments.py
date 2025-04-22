import pydantic
import typing
import typing_extensions


class AccountCreateBodyCapabilitiesBlikPayments(typing_extensions.TypedDict):
    """
    AccountCreateBodyCapabilitiesBlikPayments
    """

    requested: typing_extensions.NotRequired[bool]


class _SerializerAccountCreateBodyCapabilitiesBlikPayments(pydantic.BaseModel):
    """
    Serializer for AccountCreateBodyCapabilitiesBlikPayments handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    requested: typing.Optional[bool] = pydantic.Field(alias="requested", default=None)
