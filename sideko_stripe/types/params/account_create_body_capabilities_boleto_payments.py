import pydantic
import typing
import typing_extensions


class AccountCreateBodyCapabilitiesBoletoPayments(typing_extensions.TypedDict):
    """
    AccountCreateBodyCapabilitiesBoletoPayments
    """

    requested: typing_extensions.NotRequired[bool]


class _SerializerAccountCreateBodyCapabilitiesBoletoPayments(pydantic.BaseModel):
    """
    Serializer for AccountCreateBodyCapabilitiesBoletoPayments handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    requested: typing.Optional[bool] = pydantic.Field(alias="requested", default=None)
