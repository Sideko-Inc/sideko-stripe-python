import pydantic
import typing
import typing_extensions


class AccountUpdateBodyCapabilitiesP24Payments(typing_extensions.TypedDict):
    """
    AccountUpdateBodyCapabilitiesP24Payments
    """

    requested: typing_extensions.NotRequired[bool]


class _SerializerAccountUpdateBodyCapabilitiesP24Payments(pydantic.BaseModel):
    """
    Serializer for AccountUpdateBodyCapabilitiesP24Payments handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    requested: typing.Optional[bool] = pydantic.Field(alias="requested", default=None)
