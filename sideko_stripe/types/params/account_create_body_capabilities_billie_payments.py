import pydantic
import typing
import typing_extensions


class AccountCreateBodyCapabilitiesBilliePayments(typing_extensions.TypedDict):
    """
    AccountCreateBodyCapabilitiesBilliePayments
    """

    requested: typing_extensions.NotRequired[bool]


class _SerializerAccountCreateBodyCapabilitiesBilliePayments(pydantic.BaseModel):
    """
    Serializer for AccountCreateBodyCapabilitiesBilliePayments handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    requested: typing.Optional[bool] = pydantic.Field(alias="requested", default=None)
