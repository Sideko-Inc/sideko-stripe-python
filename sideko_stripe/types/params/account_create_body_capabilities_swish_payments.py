import pydantic
import typing
import typing_extensions


class AccountCreateBodyCapabilitiesSwishPayments(typing_extensions.TypedDict):
    """
    AccountCreateBodyCapabilitiesSwishPayments
    """

    requested: typing_extensions.NotRequired[bool]


class _SerializerAccountCreateBodyCapabilitiesSwishPayments(pydantic.BaseModel):
    """
    Serializer for AccountCreateBodyCapabilitiesSwishPayments handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    requested: typing.Optional[bool] = pydantic.Field(alias="requested", default=None)
