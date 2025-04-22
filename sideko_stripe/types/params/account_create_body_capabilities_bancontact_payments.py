import pydantic
import typing
import typing_extensions


class AccountCreateBodyCapabilitiesBancontactPayments(typing_extensions.TypedDict):
    """
    AccountCreateBodyCapabilitiesBancontactPayments
    """

    requested: typing_extensions.NotRequired[bool]


class _SerializerAccountCreateBodyCapabilitiesBancontactPayments(pydantic.BaseModel):
    """
    Serializer for AccountCreateBodyCapabilitiesBancontactPayments handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    requested: typing.Optional[bool] = pydantic.Field(alias="requested", default=None)
