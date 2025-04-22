import pydantic
import typing
import typing_extensions


class TreasuryOutboundTransferCreateBodyDestinationPaymentMethodData(
    typing_extensions.TypedDict
):
    """
    Hash used to generate the PaymentMethod to be used for this OutboundTransfer. Exclusive with `destination_payment_method`.
    """

    financial_account: typing_extensions.NotRequired[str]

    type_: typing_extensions.Required[typing_extensions.Literal["financial_account"]]


class _SerializerTreasuryOutboundTransferCreateBodyDestinationPaymentMethodData(
    pydantic.BaseModel
):
    """
    Serializer for TreasuryOutboundTransferCreateBodyDestinationPaymentMethodData handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    financial_account: typing.Optional[str] = pydantic.Field(
        alias="financial_account", default=None
    )
    type_: typing_extensions.Literal["financial_account"] = pydantic.Field(
        alias="type",
    )
