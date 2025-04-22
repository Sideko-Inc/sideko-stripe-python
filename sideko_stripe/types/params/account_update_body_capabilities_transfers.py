import pydantic
import typing
import typing_extensions


class AccountUpdateBodyCapabilitiesTransfers(typing_extensions.TypedDict):
    """
    AccountUpdateBodyCapabilitiesTransfers
    """

    requested: typing_extensions.NotRequired[bool]


class _SerializerAccountUpdateBodyCapabilitiesTransfers(pydantic.BaseModel):
    """
    Serializer for AccountUpdateBodyCapabilitiesTransfers handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    requested: typing.Optional[bool] = pydantic.Field(alias="requested", default=None)
