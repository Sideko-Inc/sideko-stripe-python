import pydantic
import typing
import typing_extensions


class AccountCreateBodyCapabilitiesTransfers(typing_extensions.TypedDict):
    """
    AccountCreateBodyCapabilitiesTransfers
    """

    requested: typing_extensions.NotRequired[bool]


class _SerializerAccountCreateBodyCapabilitiesTransfers(pydantic.BaseModel):
    """
    Serializer for AccountCreateBodyCapabilitiesTransfers handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    requested: typing.Optional[bool] = pydantic.Field(alias="requested", default=None)
