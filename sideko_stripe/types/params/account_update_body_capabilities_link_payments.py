import pydantic
import typing
import typing_extensions


class AccountUpdateBodyCapabilitiesLinkPayments(typing_extensions.TypedDict):
    """
    AccountUpdateBodyCapabilitiesLinkPayments
    """

    requested: typing_extensions.NotRequired[bool]


class _SerializerAccountUpdateBodyCapabilitiesLinkPayments(pydantic.BaseModel):
    """
    Serializer for AccountUpdateBodyCapabilitiesLinkPayments handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    requested: typing.Optional[bool] = pydantic.Field(alias="requested", default=None)
