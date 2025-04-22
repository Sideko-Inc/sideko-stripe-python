import pydantic
import typing
import typing_extensions

from .dispute_update_body_evidence_enhanced_evidence_obj0 import (
    DisputeUpdateBodyEvidenceEnhancedEvidenceObj0,
    _SerializerDisputeUpdateBodyEvidenceEnhancedEvidenceObj0,
)


class DisputeUpdateBodyEvidence(typing_extensions.TypedDict):
    """
    Evidence to upload, to respond to a dispute. Updating any field in the hash will submit all fields in the hash for review. The combined character count of all fields is limited to 150,000.
    """

    access_activity_log: typing_extensions.NotRequired[str]

    billing_address: typing_extensions.NotRequired[str]

    cancellation_policy: typing_extensions.NotRequired[str]

    cancellation_policy_disclosure: typing_extensions.NotRequired[str]

    cancellation_rebuttal: typing_extensions.NotRequired[str]

    customer_communication: typing_extensions.NotRequired[str]

    customer_email_address: typing_extensions.NotRequired[str]

    customer_name: typing_extensions.NotRequired[str]

    customer_purchase_ip: typing_extensions.NotRequired[str]

    customer_signature: typing_extensions.NotRequired[str]

    duplicate_charge_documentation: typing_extensions.NotRequired[str]

    duplicate_charge_explanation: typing_extensions.NotRequired[str]

    duplicate_charge_id: typing_extensions.NotRequired[str]

    enhanced_evidence: typing_extensions.NotRequired[
        typing.Union[DisputeUpdateBodyEvidenceEnhancedEvidenceObj0, str]
    ]

    product_description: typing_extensions.NotRequired[str]

    receipt: typing_extensions.NotRequired[str]

    refund_policy: typing_extensions.NotRequired[str]

    refund_policy_disclosure: typing_extensions.NotRequired[str]

    refund_refusal_explanation: typing_extensions.NotRequired[str]

    service_date: typing_extensions.NotRequired[str]

    service_documentation: typing_extensions.NotRequired[str]

    shipping_address: typing_extensions.NotRequired[str]

    shipping_carrier: typing_extensions.NotRequired[str]

    shipping_date: typing_extensions.NotRequired[str]

    shipping_documentation: typing_extensions.NotRequired[str]

    shipping_tracking_number: typing_extensions.NotRequired[str]

    uncategorized_file: typing_extensions.NotRequired[str]

    uncategorized_text: typing_extensions.NotRequired[str]


class _SerializerDisputeUpdateBodyEvidence(pydantic.BaseModel):
    """
    Serializer for DisputeUpdateBodyEvidence handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    access_activity_log: typing.Optional[str] = pydantic.Field(
        alias="access_activity_log", default=None
    )
    billing_address: typing.Optional[str] = pydantic.Field(
        alias="billing_address", default=None
    )
    cancellation_policy: typing.Optional[str] = pydantic.Field(
        alias="cancellation_policy", default=None
    )
    cancellation_policy_disclosure: typing.Optional[str] = pydantic.Field(
        alias="cancellation_policy_disclosure", default=None
    )
    cancellation_rebuttal: typing.Optional[str] = pydantic.Field(
        alias="cancellation_rebuttal", default=None
    )
    customer_communication: typing.Optional[str] = pydantic.Field(
        alias="customer_communication", default=None
    )
    customer_email_address: typing.Optional[str] = pydantic.Field(
        alias="customer_email_address", default=None
    )
    customer_name: typing.Optional[str] = pydantic.Field(
        alias="customer_name", default=None
    )
    customer_purchase_ip: typing.Optional[str] = pydantic.Field(
        alias="customer_purchase_ip", default=None
    )
    customer_signature: typing.Optional[str] = pydantic.Field(
        alias="customer_signature", default=None
    )
    duplicate_charge_documentation: typing.Optional[str] = pydantic.Field(
        alias="duplicate_charge_documentation", default=None
    )
    duplicate_charge_explanation: typing.Optional[str] = pydantic.Field(
        alias="duplicate_charge_explanation", default=None
    )
    duplicate_charge_id: typing.Optional[str] = pydantic.Field(
        alias="duplicate_charge_id", default=None
    )
    enhanced_evidence: typing.Optional[
        typing.Union[_SerializerDisputeUpdateBodyEvidenceEnhancedEvidenceObj0, str]
    ] = pydantic.Field(alias="enhanced_evidence", default=None)
    product_description: typing.Optional[str] = pydantic.Field(
        alias="product_description", default=None
    )
    receipt: typing.Optional[str] = pydantic.Field(alias="receipt", default=None)
    refund_policy: typing.Optional[str] = pydantic.Field(
        alias="refund_policy", default=None
    )
    refund_policy_disclosure: typing.Optional[str] = pydantic.Field(
        alias="refund_policy_disclosure", default=None
    )
    refund_refusal_explanation: typing.Optional[str] = pydantic.Field(
        alias="refund_refusal_explanation", default=None
    )
    service_date: typing.Optional[str] = pydantic.Field(
        alias="service_date", default=None
    )
    service_documentation: typing.Optional[str] = pydantic.Field(
        alias="service_documentation", default=None
    )
    shipping_address: typing.Optional[str] = pydantic.Field(
        alias="shipping_address", default=None
    )
    shipping_carrier: typing.Optional[str] = pydantic.Field(
        alias="shipping_carrier", default=None
    )
    shipping_date: typing.Optional[str] = pydantic.Field(
        alias="shipping_date", default=None
    )
    shipping_documentation: typing.Optional[str] = pydantic.Field(
        alias="shipping_documentation", default=None
    )
    shipping_tracking_number: typing.Optional[str] = pydantic.Field(
        alias="shipping_tracking_number", default=None
    )
    uncategorized_file: typing.Optional[str] = pydantic.Field(
        alias="uncategorized_file", default=None
    )
    uncategorized_text: typing.Optional[str] = pydantic.Field(
        alias="uncategorized_text", default=None
    )
