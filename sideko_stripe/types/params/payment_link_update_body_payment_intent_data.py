import pydantic
import typing
import typing_extensions

from .payment_link_update_body_payment_intent_data_metadata_obj0 import (
    PaymentLinkUpdateBodyPaymentIntentDataMetadataObj0,
    _SerializerPaymentLinkUpdateBodyPaymentIntentDataMetadataObj0,
)


class PaymentLinkUpdateBodyPaymentIntentData(typing_extensions.TypedDict):
    """
    A subset of parameters to be passed to PaymentIntent creation for Checkout Sessions in `payment` mode.
    """

    description: typing_extensions.NotRequired[typing.Union[str, str]]

    metadata: typing_extensions.NotRequired[
        typing.Union[PaymentLinkUpdateBodyPaymentIntentDataMetadataObj0, str]
    ]

    statement_descriptor: typing_extensions.NotRequired[typing.Union[str, str]]

    statement_descriptor_suffix: typing_extensions.NotRequired[typing.Union[str, str]]

    transfer_group: typing_extensions.NotRequired[typing.Union[str, str]]


class _SerializerPaymentLinkUpdateBodyPaymentIntentData(pydantic.BaseModel):
    """
    Serializer for PaymentLinkUpdateBodyPaymentIntentData handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    description: typing.Optional[typing.Union[str, str]] = pydantic.Field(
        alias="description", default=None
    )
    metadata: typing.Optional[
        typing.Union[_SerializerPaymentLinkUpdateBodyPaymentIntentDataMetadataObj0, str]
    ] = pydantic.Field(alias="metadata", default=None)
    statement_descriptor: typing.Optional[typing.Union[str, str]] = pydantic.Field(
        alias="statement_descriptor", default=None
    )
    statement_descriptor_suffix: typing.Optional[typing.Union[str, str]] = (
        pydantic.Field(alias="statement_descriptor_suffix", default=None)
    )
    transfer_group: typing.Optional[typing.Union[str, str]] = pydantic.Field(
        alias="transfer_group", default=None
    )
