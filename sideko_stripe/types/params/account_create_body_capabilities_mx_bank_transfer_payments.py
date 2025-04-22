import pydantic
import typing
import typing_extensions


class AccountCreateBodyCapabilitiesMxBankTransferPayments(typing_extensions.TypedDict):
    """
    AccountCreateBodyCapabilitiesMxBankTransferPayments
    """

    requested: typing_extensions.NotRequired[bool]


class _SerializerAccountCreateBodyCapabilitiesMxBankTransferPayments(
    pydantic.BaseModel
):
    """
    Serializer for AccountCreateBodyCapabilitiesMxBankTransferPayments handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    requested: typing.Optional[bool] = pydantic.Field(alias="requested", default=None)
