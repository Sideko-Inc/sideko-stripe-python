import pydantic
import typing
import typing_extensions

from .charge_dispute_create_body_evidence_enhanced_evidence_obj0_visa_compelling_evidence3_disputed_transaction_shipping_address import (
    ChargeDisputeCreateBodyEvidenceEnhancedEvidenceObj0VisaCompellingEvidence3DisputedTransactionShippingAddress,
    _SerializerChargeDisputeCreateBodyEvidenceEnhancedEvidenceObj0VisaCompellingEvidence3DisputedTransactionShippingAddress,
)


class ChargeDisputeCreateBodyEvidenceEnhancedEvidenceObj0VisaCompellingEvidence3DisputedTransaction(
    typing_extensions.TypedDict
):
    """
    ChargeDisputeCreateBodyEvidenceEnhancedEvidenceObj0VisaCompellingEvidence3DisputedTransaction
    """

    customer_account_id: typing_extensions.NotRequired[typing.Union[str, str]]

    customer_device_fingerprint: typing_extensions.NotRequired[typing.Union[str, str]]

    customer_device_id: typing_extensions.NotRequired[typing.Union[str, str]]

    customer_email_address: typing_extensions.NotRequired[typing.Union[str, str]]

    customer_purchase_ip: typing_extensions.NotRequired[typing.Union[str, str]]

    merchandise_or_services: typing_extensions.NotRequired[
        typing_extensions.Literal["merchandise", "services"]
    ]

    product_description: typing_extensions.NotRequired[typing.Union[str, str]]

    shipping_address: typing_extensions.NotRequired[
        ChargeDisputeCreateBodyEvidenceEnhancedEvidenceObj0VisaCompellingEvidence3DisputedTransactionShippingAddress
    ]


class _SerializerChargeDisputeCreateBodyEvidenceEnhancedEvidenceObj0VisaCompellingEvidence3DisputedTransaction(
    pydantic.BaseModel
):
    """
    Serializer for ChargeDisputeCreateBodyEvidenceEnhancedEvidenceObj0VisaCompellingEvidence3DisputedTransaction handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    customer_account_id: typing.Optional[typing.Union[str, str]] = pydantic.Field(
        alias="customer_account_id", default=None
    )
    customer_device_fingerprint: typing.Optional[typing.Union[str, str]] = (
        pydantic.Field(alias="customer_device_fingerprint", default=None)
    )
    customer_device_id: typing.Optional[typing.Union[str, str]] = pydantic.Field(
        alias="customer_device_id", default=None
    )
    customer_email_address: typing.Optional[typing.Union[str, str]] = pydantic.Field(
        alias="customer_email_address", default=None
    )
    customer_purchase_ip: typing.Optional[typing.Union[str, str]] = pydantic.Field(
        alias="customer_purchase_ip", default=None
    )
    merchandise_or_services: typing.Optional[
        typing_extensions.Literal["merchandise", "services"]
    ] = pydantic.Field(alias="merchandise_or_services", default=None)
    product_description: typing.Optional[typing.Union[str, str]] = pydantic.Field(
        alias="product_description", default=None
    )
    shipping_address: typing.Optional[
        _SerializerChargeDisputeCreateBodyEvidenceEnhancedEvidenceObj0VisaCompellingEvidence3DisputedTransactionShippingAddress
    ] = pydantic.Field(alias="shipping_address", default=None)
