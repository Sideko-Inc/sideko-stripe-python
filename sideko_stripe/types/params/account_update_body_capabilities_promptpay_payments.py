import pydantic
import typing
import typing_extensions


class AccountUpdateBodyCapabilitiesPromptpayPayments(typing_extensions.TypedDict):
    """
    AccountUpdateBodyCapabilitiesPromptpayPayments
    """

    requested: typing_extensions.NotRequired[bool]


class _SerializerAccountUpdateBodyCapabilitiesPromptpayPayments(pydantic.BaseModel):
    """
    Serializer for AccountUpdateBodyCapabilitiesPromptpayPayments handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    requested: typing.Optional[bool] = pydantic.Field(alias="requested", default=None)
