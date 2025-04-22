import pydantic
import typing
import typing_extensions


class AccountUpdateBodyCapabilitiesBankTransferPayments(typing_extensions.TypedDict):
    """
    AccountUpdateBodyCapabilitiesBankTransferPayments
    """

    requested: typing_extensions.NotRequired[bool]


class _SerializerAccountUpdateBodyCapabilitiesBankTransferPayments(pydantic.BaseModel):
    """
    Serializer for AccountUpdateBodyCapabilitiesBankTransferPayments handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    requested: typing.Optional[bool] = pydantic.Field(alias="requested", default=None)
