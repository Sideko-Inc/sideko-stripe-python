import pydantic
import typing
import typing_extensions


class AccountCreateBodyCapabilitiesKrCardPayments(typing_extensions.TypedDict):
    """
    AccountCreateBodyCapabilitiesKrCardPayments
    """

    requested: typing_extensions.NotRequired[bool]


class _SerializerAccountCreateBodyCapabilitiesKrCardPayments(pydantic.BaseModel):
    """
    Serializer for AccountCreateBodyCapabilitiesKrCardPayments handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    requested: typing.Optional[bool] = pydantic.Field(alias="requested", default=None)
