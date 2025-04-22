import pydantic
import typing
import typing_extensions


class AccountUpdateBodyCapabilitiesMxBankTransferPayments(typing_extensions.TypedDict):
    """
    AccountUpdateBodyCapabilitiesMxBankTransferPayments
    """

    requested: typing_extensions.NotRequired[bool]


class _SerializerAccountUpdateBodyCapabilitiesMxBankTransferPayments(
    pydantic.BaseModel
):
    """
    Serializer for AccountUpdateBodyCapabilitiesMxBankTransferPayments handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    requested: typing.Optional[bool] = pydantic.Field(alias="requested", default=None)
