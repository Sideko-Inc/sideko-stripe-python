import pydantic
import typing
import typing_extensions

from .dispute_enhanced_evidence import DisputeEnhancedEvidence

if typing_extensions.TYPE_CHECKING:
    from .file import File


class DisputeEvidence(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    access_activity_log: typing.Optional[str] = pydantic.Field(
        alias="access_activity_log", default=None
    )
    """
    Any server or activity logs showing proof that the customer accessed or downloaded the purchased digital product. This information should include IP addresses, corresponding timestamps, and any detailed recorded activity.
    """
    billing_address: typing.Optional[str] = pydantic.Field(
        alias="billing_address", default=None
    )
    """
    The billing address provided by the customer.
    """
    cancellation_policy: typing.Optional[typing.Union[str, "File"]] = pydantic.Field(
        alias="cancellation_policy", default=None
    )
    """
    (ID of a [file upload](https://stripe.com/docs/guides/file-upload)) Your subscription cancellation policy, as shown to the customer.
    """
    cancellation_policy_disclosure: typing.Optional[str] = pydantic.Field(
        alias="cancellation_policy_disclosure", default=None
    )
    """
    An explanation of how and when the customer was shown your refund policy prior to purchase.
    """
    cancellation_rebuttal: typing.Optional[str] = pydantic.Field(
        alias="cancellation_rebuttal", default=None
    )
    """
    A justification for why the customer's subscription was not canceled.
    """
    customer_communication: typing.Optional[typing.Union[str, "File"]] = pydantic.Field(
        alias="customer_communication", default=None
    )
    """
    (ID of a [file upload](https://stripe.com/docs/guides/file-upload)) Any communication with the customer that you feel is relevant to your case. Examples include emails proving that the customer received the product or service, or demonstrating their use of or satisfaction with the product or service.
    """
    customer_email_address: typing.Optional[str] = pydantic.Field(
        alias="customer_email_address", default=None
    )
    """
    The email address of the customer.
    """
    customer_name: typing.Optional[str] = pydantic.Field(
        alias="customer_name", default=None
    )
    """
    The name of the customer.
    """
    customer_purchase_ip: typing.Optional[str] = pydantic.Field(
        alias="customer_purchase_ip", default=None
    )
    """
    The IP address that the customer used when making the purchase.
    """
    customer_signature: typing.Optional[typing.Union[str, "File"]] = pydantic.Field(
        alias="customer_signature", default=None
    )
    """
    (ID of a [file upload](https://stripe.com/docs/guides/file-upload)) A relevant document or contract showing the customer's signature.
    """
    duplicate_charge_documentation: typing.Optional[typing.Union[str, "File"]] = (
        pydantic.Field(alias="duplicate_charge_documentation", default=None)
    )
    """
    (ID of a [file upload](https://stripe.com/docs/guides/file-upload)) Documentation for the prior charge that can uniquely identify the charge, such as a receipt, shipping label, work order, etc. This document should be paired with a similar document from the disputed payment that proves the two payments are separate.
    """
    duplicate_charge_explanation: typing.Optional[str] = pydantic.Field(
        alias="duplicate_charge_explanation", default=None
    )
    """
    An explanation of the difference between the disputed charge versus the prior charge that appears to be a duplicate.
    """
    duplicate_charge_id: typing.Optional[str] = pydantic.Field(
        alias="duplicate_charge_id", default=None
    )
    """
    The Stripe ID for the prior charge which appears to be a duplicate of the disputed charge.
    """
    enhanced_evidence: DisputeEnhancedEvidence = pydantic.Field(
        alias="enhanced_evidence",
    )
    product_description: typing.Optional[str] = pydantic.Field(
        alias="product_description", default=None
    )
    """
    A description of the product or service that was sold.
    """
    receipt: typing.Optional[typing.Union[str, "File"]] = pydantic.Field(
        alias="receipt", default=None
    )
    """
    (ID of a [file upload](https://stripe.com/docs/guides/file-upload)) Any receipt or message sent to the customer notifying them of the charge.
    """
    refund_policy: typing.Optional[typing.Union[str, "File"]] = pydantic.Field(
        alias="refund_policy", default=None
    )
    """
    (ID of a [file upload](https://stripe.com/docs/guides/file-upload)) Your refund policy, as shown to the customer.
    """
    refund_policy_disclosure: typing.Optional[str] = pydantic.Field(
        alias="refund_policy_disclosure", default=None
    )
    """
    Documentation demonstrating that the customer was shown your refund policy prior to purchase.
    """
    refund_refusal_explanation: typing.Optional[str] = pydantic.Field(
        alias="refund_refusal_explanation", default=None
    )
    """
    A justification for why the customer is not entitled to a refund.
    """
    service_date: typing.Optional[str] = pydantic.Field(
        alias="service_date", default=None
    )
    """
    The date on which the customer received or began receiving the purchased service, in a clear human-readable format.
    """
    service_documentation: typing.Optional[typing.Union[str, "File"]] = pydantic.Field(
        alias="service_documentation", default=None
    )
    """
    (ID of a [file upload](https://stripe.com/docs/guides/file-upload)) Documentation showing proof that a service was provided to the customer. This could include a copy of a signed contract, work order, or other form of written agreement.
    """
    shipping_address: typing.Optional[str] = pydantic.Field(
        alias="shipping_address", default=None
    )
    """
    The address to which a physical product was shipped. You should try to include as complete address information as possible.
    """
    shipping_carrier: typing.Optional[str] = pydantic.Field(
        alias="shipping_carrier", default=None
    )
    """
    The delivery service that shipped a physical product, such as Fedex, UPS, USPS, etc. If multiple carriers were used for this purchase, please separate them with commas.
    """
    shipping_date: typing.Optional[str] = pydantic.Field(
        alias="shipping_date", default=None
    )
    """
    The date on which a physical product began its route to the shipping address, in a clear human-readable format.
    """
    shipping_documentation: typing.Optional[typing.Union[str, "File"]] = pydantic.Field(
        alias="shipping_documentation", default=None
    )
    """
    (ID of a [file upload](https://stripe.com/docs/guides/file-upload)) Documentation showing proof that a product was shipped to the customer at the same address the customer provided to you. This could include a copy of the shipment receipt, shipping label, etc. It should show the customer's full shipping address, if possible.
    """
    shipping_tracking_number: typing.Optional[str] = pydantic.Field(
        alias="shipping_tracking_number", default=None
    )
    """
    The tracking number for a physical product, obtained from the delivery service. If multiple tracking numbers were generated for this purchase, please separate them with commas.
    """
    uncategorized_file: typing.Optional[typing.Union[str, "File"]] = pydantic.Field(
        alias="uncategorized_file", default=None
    )
    """
    (ID of a [file upload](https://stripe.com/docs/guides/file-upload)) Any additional evidence or statements.
    """
    uncategorized_text: typing.Optional[str] = pydantic.Field(
        alias="uncategorized_text", default=None
    )
    """
    Any additional evidence or statements.
    """
