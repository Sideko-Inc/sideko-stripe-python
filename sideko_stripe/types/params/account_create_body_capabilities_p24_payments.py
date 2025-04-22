import pydantic
import typing
import typing_extensions


class AccountCreateBodyCapabilitiesP24Payments(typing_extensions.TypedDict):
    """
    AccountCreateBodyCapabilitiesP24Payments
    """

    requested: typing_extensions.NotRequired[bool]


class _SerializerAccountCreateBodyCapabilitiesP24Payments(pydantic.BaseModel):
    """
    Serializer for AccountCreateBodyCapabilitiesP24Payments handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    requested: typing.Optional[bool] = pydantic.Field(alias="requested", default=None)
