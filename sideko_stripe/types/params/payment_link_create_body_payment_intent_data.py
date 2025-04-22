import pydantic
import typing
import typing_extensions

from .payment_link_create_body_payment_intent_data_metadata import (
    PaymentLinkCreateBodyPaymentIntentDataMetadata,
    _SerializerPaymentLinkCreateBodyPaymentIntentDataMetadata,
)


class PaymentLinkCreateBodyPaymentIntentData(typing_extensions.TypedDict):
    """
    A subset of parameters to be passed to PaymentIntent creation for Checkout Sessions in `payment` mode.
    """

    capture_method: typing_extensions.NotRequired[
        typing_extensions.Literal["automatic", "automatic_async", "manual"]
    ]

    description: typing_extensions.NotRequired[str]

    metadata: typing_extensions.NotRequired[
        PaymentLinkCreateBodyPaymentIntentDataMetadata
    ]

    setup_future_usage: typing_extensions.NotRequired[
        typing_extensions.Literal["off_session", "on_session"]
    ]

    statement_descriptor: typing_extensions.NotRequired[str]

    statement_descriptor_suffix: typing_extensions.NotRequired[str]

    transfer_group: typing_extensions.NotRequired[str]


class _SerializerPaymentLinkCreateBodyPaymentIntentData(pydantic.BaseModel):
    """
    Serializer for PaymentLinkCreateBodyPaymentIntentData handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    capture_method: typing.Optional[
        typing_extensions.Literal["automatic", "automatic_async", "manual"]
    ] = pydantic.Field(alias="capture_method", default=None)
    description: typing.Optional[str] = pydantic.Field(
        alias="description", default=None
    )
    metadata: typing.Optional[
        _SerializerPaymentLinkCreateBodyPaymentIntentDataMetadata
    ] = pydantic.Field(alias="metadata", default=None)
    setup_future_usage: typing.Optional[
        typing_extensions.Literal["off_session", "on_session"]
    ] = pydantic.Field(alias="setup_future_usage", default=None)
    statement_descriptor: typing.Optional[str] = pydantic.Field(
        alias="statement_descriptor", default=None
    )
    statement_descriptor_suffix: typing.Optional[str] = pydantic.Field(
        alias="statement_descriptor_suffix", default=None
    )
    transfer_group: typing.Optional[str] = pydantic.Field(
        alias="transfer_group", default=None
    )
