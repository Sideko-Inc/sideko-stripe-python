import pydantic
import typing
import typing_extensions


class AccountUpdateBodyCapabilitiesJpBankTransferPayments(typing_extensions.TypedDict):
    """
    AccountUpdateBodyCapabilitiesJpBankTransferPayments
    """

    requested: typing_extensions.NotRequired[bool]


class _SerializerAccountUpdateBodyCapabilitiesJpBankTransferPayments(
    pydantic.BaseModel
):
    """
    Serializer for AccountUpdateBodyCapabilitiesJpBankTransferPayments handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    requested: typing.Optional[bool] = pydantic.Field(alias="requested", default=None)
