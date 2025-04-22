import pydantic
import typing
import typing_extensions


class TreasuryOutboundPaymentCreateBodyDestinationPaymentMethodOptionsUsBankAccountObj0(
    typing_extensions.TypedDict
):
    """
    TreasuryOutboundPaymentCreateBodyDestinationPaymentMethodOptionsUsBankAccountObj0
    """

    network: typing_extensions.NotRequired[
        typing_extensions.Literal["ach", "us_domestic_wire"]
    ]


class _SerializerTreasuryOutboundPaymentCreateBodyDestinationPaymentMethodOptionsUsBankAccountObj0(
    pydantic.BaseModel
):
    """
    Serializer for TreasuryOutboundPaymentCreateBodyDestinationPaymentMethodOptionsUsBankAccountObj0 handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    network: typing.Optional[typing_extensions.Literal["ach", "us_domestic_wire"]] = (
        pydantic.Field(alias="network", default=None)
    )
