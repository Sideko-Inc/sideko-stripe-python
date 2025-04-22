import pydantic
import typing
import typing_extensions


class TreasuryOutboundPaymentCreateBodyDestinationPaymentMethodDataMetadata(
    typing_extensions.TypedDict, total=False
):
    """
    TreasuryOutboundPaymentCreateBodyDestinationPaymentMethodDataMetadata
    """


class _SerializerTreasuryOutboundPaymentCreateBodyDestinationPaymentMethodDataMetadata(
    pydantic.BaseModel
):
    """
    Serializer for TreasuryOutboundPaymentCreateBodyDestinationPaymentMethodDataMetadata handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, str]
