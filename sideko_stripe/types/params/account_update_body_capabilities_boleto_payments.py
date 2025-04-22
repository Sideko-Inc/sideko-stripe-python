import pydantic
import typing
import typing_extensions


class AccountUpdateBodyCapabilitiesBoletoPayments(typing_extensions.TypedDict):
    """
    AccountUpdateBodyCapabilitiesBoletoPayments
    """

    requested: typing_extensions.NotRequired[bool]


class _SerializerAccountUpdateBodyCapabilitiesBoletoPayments(pydantic.BaseModel):
    """
    Serializer for AccountUpdateBodyCapabilitiesBoletoPayments handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    requested: typing.Optional[bool] = pydantic.Field(alias="requested", default=None)
