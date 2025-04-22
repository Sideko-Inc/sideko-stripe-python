import pydantic
import typing
import typing_extensions


class AccountCreateBodyCapabilitiesGiropayPayments(typing_extensions.TypedDict):
    """
    AccountCreateBodyCapabilitiesGiropayPayments
    """

    requested: typing_extensions.NotRequired[bool]


class _SerializerAccountCreateBodyCapabilitiesGiropayPayments(pydantic.BaseModel):
    """
    Serializer for AccountCreateBodyCapabilitiesGiropayPayments handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    requested: typing.Optional[bool] = pydantic.Field(alias="requested", default=None)
