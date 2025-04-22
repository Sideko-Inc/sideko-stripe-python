import pydantic
import typing
import typing_extensions


class AccountCreateBodyCapabilitiesUsBankTransferPayments(typing_extensions.TypedDict):
    """
    AccountCreateBodyCapabilitiesUsBankTransferPayments
    """

    requested: typing_extensions.NotRequired[bool]


class _SerializerAccountCreateBodyCapabilitiesUsBankTransferPayments(
    pydantic.BaseModel
):
    """
    Serializer for AccountCreateBodyCapabilitiesUsBankTransferPayments handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    requested: typing.Optional[bool] = pydantic.Field(alias="requested", default=None)
