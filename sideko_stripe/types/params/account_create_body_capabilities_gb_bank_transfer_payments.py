import pydantic
import typing
import typing_extensions


class AccountCreateBodyCapabilitiesGbBankTransferPayments(typing_extensions.TypedDict):
    """
    AccountCreateBodyCapabilitiesGbBankTransferPayments
    """

    requested: typing_extensions.NotRequired[bool]


class _SerializerAccountCreateBodyCapabilitiesGbBankTransferPayments(
    pydantic.BaseModel
):
    """
    Serializer for AccountCreateBodyCapabilitiesGbBankTransferPayments handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    requested: typing.Optional[bool] = pydantic.Field(alias="requested", default=None)
