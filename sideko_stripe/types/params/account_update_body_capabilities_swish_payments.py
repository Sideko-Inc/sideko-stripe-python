import pydantic
import typing
import typing_extensions


class AccountUpdateBodyCapabilitiesSwishPayments(typing_extensions.TypedDict):
    """
    AccountUpdateBodyCapabilitiesSwishPayments
    """

    requested: typing_extensions.NotRequired[bool]


class _SerializerAccountUpdateBodyCapabilitiesSwishPayments(pydantic.BaseModel):
    """
    Serializer for AccountUpdateBodyCapabilitiesSwishPayments handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    requested: typing.Optional[bool] = pydantic.Field(alias="requested", default=None)
