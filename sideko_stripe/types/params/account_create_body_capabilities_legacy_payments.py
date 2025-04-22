import pydantic
import typing
import typing_extensions


class AccountCreateBodyCapabilitiesLegacyPayments(typing_extensions.TypedDict):
    """
    AccountCreateBodyCapabilitiesLegacyPayments
    """

    requested: typing_extensions.NotRequired[bool]


class _SerializerAccountCreateBodyCapabilitiesLegacyPayments(pydantic.BaseModel):
    """
    Serializer for AccountCreateBodyCapabilitiesLegacyPayments handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    requested: typing.Optional[bool] = pydantic.Field(alias="requested", default=None)
