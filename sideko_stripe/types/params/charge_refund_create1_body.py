import pydantic
import typing
import typing_extensions

from .charge_refund_create1_body_metadata_obj0 import (
    ChargeRefundCreate1BodyMetadataObj0,
    _SerializerChargeRefundCreate1BodyMetadataObj0,
)


class ChargeRefundCreate1Body(typing_extensions.TypedDict, total=False):
    """
    ChargeRefundCreate1Body
    """

    amount: typing_extensions.NotRequired[int]

    currency: typing_extensions.NotRequired[str]
    """
    Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
    """

    customer: typing_extensions.NotRequired[str]
    """
    Customer whose customer balance to refund from.
    """

    expand: typing_extensions.NotRequired[typing.List[str]]
    """
    Specifies which fields in the response should be expanded.
    """

    instructions_email: typing_extensions.NotRequired[str]
    """
    For payment methods without native refund support (e.g., Konbini, PromptPay), use this email from the customer to receive refund instructions.
    """

    metadata: typing_extensions.NotRequired[
        typing.Union[ChargeRefundCreate1BodyMetadataObj0, str]
    ]
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    """

    origin: typing_extensions.NotRequired[typing_extensions.Literal["customer_balance"]]
    """
    Origin of the refund
    """

    payment_intent: typing_extensions.NotRequired[str]
    """
    The identifier of the PaymentIntent to refund.
    """

    reason: typing_extensions.NotRequired[
        typing_extensions.Literal["duplicate", "fraudulent", "requested_by_customer"]
    ]
    """
    String indicating the reason for the refund. If set, possible values are `duplicate`, `fraudulent`, and `requested_by_customer`. If you believe the charge to be fraudulent, specifying `fraudulent` as the reason will add the associated card and email to your [block lists](https://stripe.com/docs/radar/lists), and will also help us improve our fraud detection algorithms.
    """

    refund_application_fee: typing_extensions.NotRequired[bool]
    """
    Boolean indicating whether the application fee should be refunded when refunding this charge. If a full charge refund is given, the full application fee will be refunded. Otherwise, the application fee will be refunded in an amount proportional to the amount of the charge refunded. An application fee can be refunded only by the application that created the charge.
    """

    reverse_transfer: typing_extensions.NotRequired[bool]
    """
    Boolean indicating whether the transfer should be reversed when refunding this charge. The transfer will be reversed proportionally to the amount being refunded (either the entire or partial amount).<br><br>A transfer can be reversed only by the application that created the charge.
    """


class _SerializerChargeRefundCreate1Body(pydantic.BaseModel):
    """
    Serializer for ChargeRefundCreate1Body handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, typing.Any]

    amount: typing.Optional[int] = pydantic.Field(alias="amount", default=None)
    currency: typing.Optional[str] = pydantic.Field(alias="currency", default=None)
    customer: typing.Optional[str] = pydantic.Field(alias="customer", default=None)
    expand: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="expand", default=None
    )
    instructions_email: typing.Optional[str] = pydantic.Field(
        alias="instructions_email", default=None
    )
    metadata: typing.Optional[
        typing.Union[_SerializerChargeRefundCreate1BodyMetadataObj0, str]
    ] = pydantic.Field(alias="metadata", default=None)
    origin: typing.Optional[typing_extensions.Literal["customer_balance"]] = (
        pydantic.Field(alias="origin", default=None)
    )
    payment_intent: typing.Optional[str] = pydantic.Field(
        alias="payment_intent", default=None
    )
    reason: typing.Optional[
        typing_extensions.Literal["duplicate", "fraudulent", "requested_by_customer"]
    ] = pydantic.Field(alias="reason", default=None)
    refund_application_fee: typing.Optional[bool] = pydantic.Field(
        alias="refund_application_fee", default=None
    )
    reverse_transfer: typing.Optional[bool] = pydantic.Field(
        alias="reverse_transfer", default=None
    )
