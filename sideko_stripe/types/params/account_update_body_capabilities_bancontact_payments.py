import pydantic
import typing
import typing_extensions


class AccountUpdateBodyCapabilitiesBancontactPayments(typing_extensions.TypedDict):
    """
    AccountUpdateBodyCapabilitiesBancontactPayments
    """

    requested: typing_extensions.NotRequired[bool]


class _SerializerAccountUpdateBodyCapabilitiesBancontactPayments(pydantic.BaseModel):
    """
    Serializer for AccountUpdateBodyCapabilitiesBancontactPayments handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    requested: typing.Optional[bool] = pydantic.Field(alias="requested", default=None)
