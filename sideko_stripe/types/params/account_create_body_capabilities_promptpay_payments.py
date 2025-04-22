import pydantic
import typing
import typing_extensions


class AccountCreateBodyCapabilitiesPromptpayPayments(typing_extensions.TypedDict):
    """
    AccountCreateBodyCapabilitiesPromptpayPayments
    """

    requested: typing_extensions.NotRequired[bool]


class _SerializerAccountCreateBodyCapabilitiesPromptpayPayments(pydantic.BaseModel):
    """
    Serializer for AccountCreateBodyCapabilitiesPromptpayPayments handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    requested: typing.Optional[bool] = pydantic.Field(alias="requested", default=None)
