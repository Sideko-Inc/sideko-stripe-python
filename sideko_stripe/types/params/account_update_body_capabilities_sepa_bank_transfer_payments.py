import pydantic
import typing
import typing_extensions


class AccountUpdateBodyCapabilitiesSepaBankTransferPayments(
    typing_extensions.TypedDict
):
    """
    AccountUpdateBodyCapabilitiesSepaBankTransferPayments
    """

    requested: typing_extensions.NotRequired[bool]


class _SerializerAccountUpdateBodyCapabilitiesSepaBankTransferPayments(
    pydantic.BaseModel
):
    """
    Serializer for AccountUpdateBodyCapabilitiesSepaBankTransferPayments handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    requested: typing.Optional[bool] = pydantic.Field(alias="requested", default=None)
