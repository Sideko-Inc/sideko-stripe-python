import pydantic
import typing
import typing_extensions


class AccountCreateBodyCapabilitiesJpBankTransferPayments(typing_extensions.TypedDict):
    """
    AccountCreateBodyCapabilitiesJpBankTransferPayments
    """

    requested: typing_extensions.NotRequired[bool]


class _SerializerAccountCreateBodyCapabilitiesJpBankTransferPayments(
    pydantic.BaseModel
):
    """
    Serializer for AccountCreateBodyCapabilitiesJpBankTransferPayments handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    requested: typing.Optional[bool] = pydantic.Field(alias="requested", default=None)
