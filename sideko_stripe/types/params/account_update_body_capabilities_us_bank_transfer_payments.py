import pydantic
import typing
import typing_extensions


class AccountUpdateBodyCapabilitiesUsBankTransferPayments(typing_extensions.TypedDict):
    """
    AccountUpdateBodyCapabilitiesUsBankTransferPayments
    """

    requested: typing_extensions.NotRequired[bool]


class _SerializerAccountUpdateBodyCapabilitiesUsBankTransferPayments(
    pydantic.BaseModel
):
    """
    Serializer for AccountUpdateBodyCapabilitiesUsBankTransferPayments handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    requested: typing.Optional[bool] = pydantic.Field(alias="requested", default=None)
