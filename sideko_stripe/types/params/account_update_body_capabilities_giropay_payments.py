import pydantic
import typing
import typing_extensions


class AccountUpdateBodyCapabilitiesGiropayPayments(typing_extensions.TypedDict):
    """
    AccountUpdateBodyCapabilitiesGiropayPayments
    """

    requested: typing_extensions.NotRequired[bool]


class _SerializerAccountUpdateBodyCapabilitiesGiropayPayments(pydantic.BaseModel):
    """
    Serializer for AccountUpdateBodyCapabilitiesGiropayPayments handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    requested: typing.Optional[bool] = pydantic.Field(alias="requested", default=None)
