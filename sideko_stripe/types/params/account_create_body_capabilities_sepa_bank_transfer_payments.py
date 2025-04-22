import pydantic
import typing
import typing_extensions


class AccountCreateBodyCapabilitiesSepaBankTransferPayments(
    typing_extensions.TypedDict
):
    """
    AccountCreateBodyCapabilitiesSepaBankTransferPayments
    """

    requested: typing_extensions.NotRequired[bool]


class _SerializerAccountCreateBodyCapabilitiesSepaBankTransferPayments(
    pydantic.BaseModel
):
    """
    Serializer for AccountCreateBodyCapabilitiesSepaBankTransferPayments handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    requested: typing.Optional[bool] = pydantic.Field(alias="requested", default=None)
