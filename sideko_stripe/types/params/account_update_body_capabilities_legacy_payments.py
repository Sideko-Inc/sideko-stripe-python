import pydantic
import typing
import typing_extensions


class AccountUpdateBodyCapabilitiesLegacyPayments(typing_extensions.TypedDict):
    """
    AccountUpdateBodyCapabilitiesLegacyPayments
    """

    requested: typing_extensions.NotRequired[bool]


class _SerializerAccountUpdateBodyCapabilitiesLegacyPayments(pydantic.BaseModel):
    """
    Serializer for AccountUpdateBodyCapabilitiesLegacyPayments handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    requested: typing.Optional[bool] = pydantic.Field(alias="requested", default=None)
