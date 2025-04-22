import pydantic
import typing
import typing_extensions


class TreasuryOutboundTransferCreateBodyDestinationPaymentMethodOptionsUsBankAccountObj0(
    typing_extensions.TypedDict
):
    """
    TreasuryOutboundTransferCreateBodyDestinationPaymentMethodOptionsUsBankAccountObj0
    """

    network: typing_extensions.NotRequired[
        typing_extensions.Literal["ach", "us_domestic_wire"]
    ]


class _SerializerTreasuryOutboundTransferCreateBodyDestinationPaymentMethodOptionsUsBankAccountObj0(
    pydantic.BaseModel
):
    """
    Serializer for TreasuryOutboundTransferCreateBodyDestinationPaymentMethodOptionsUsBankAccountObj0 handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    network: typing.Optional[typing_extensions.Literal["ach", "us_domestic_wire"]] = (
        pydantic.Field(alias="network", default=None)
    )
