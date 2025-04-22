import pydantic
import typing
import typing_extensions


class AccountCreateBodyCapabilitiesBankTransferPayments(typing_extensions.TypedDict):
    """
    AccountCreateBodyCapabilitiesBankTransferPayments
    """

    requested: typing_extensions.NotRequired[bool]


class _SerializerAccountCreateBodyCapabilitiesBankTransferPayments(pydantic.BaseModel):
    """
    Serializer for AccountCreateBodyCapabilitiesBankTransferPayments handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    requested: typing.Optional[bool] = pydantic.Field(alias="requested", default=None)
