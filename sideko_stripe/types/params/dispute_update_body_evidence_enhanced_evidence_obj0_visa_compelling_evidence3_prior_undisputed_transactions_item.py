import pydantic
import typing
import typing_extensions

from .dispute_update_body_evidence_enhanced_evidence_obj0_visa_compelling_evidence3_prior_undisputed_transactions_item_shipping_address import (
    DisputeUpdateBodyEvidenceEnhancedEvidenceObj0VisaCompellingEvidence3PriorUndisputedTransactionsItemShippingAddress,
    _SerializerDisputeUpdateBodyEvidenceEnhancedEvidenceObj0VisaCompellingEvidence3PriorUndisputedTransactionsItemShippingAddress,
)


class DisputeUpdateBodyEvidenceEnhancedEvidenceObj0VisaCompellingEvidence3PriorUndisputedTransactionsItem(
    typing_extensions.TypedDict
):
    """
    DisputeUpdateBodyEvidenceEnhancedEvidenceObj0VisaCompellingEvidence3PriorUndisputedTransactionsItem
    """

    charge: typing_extensions.Required[str]

    customer_account_id: typing_extensions.NotRequired[typing.Union[str, str]]

    customer_device_fingerprint: typing_extensions.NotRequired[typing.Union[str, str]]

    customer_device_id: typing_extensions.NotRequired[typing.Union[str, str]]

    customer_email_address: typing_extensions.NotRequired[typing.Union[str, str]]

    customer_purchase_ip: typing_extensions.NotRequired[typing.Union[str, str]]

    product_description: typing_extensions.NotRequired[typing.Union[str, str]]

    shipping_address: typing_extensions.NotRequired[
        DisputeUpdateBodyEvidenceEnhancedEvidenceObj0VisaCompellingEvidence3PriorUndisputedTransactionsItemShippingAddress
    ]


class _SerializerDisputeUpdateBodyEvidenceEnhancedEvidenceObj0VisaCompellingEvidence3PriorUndisputedTransactionsItem(
    pydantic.BaseModel
):
    """
    Serializer for DisputeUpdateBodyEvidenceEnhancedEvidenceObj0VisaCompellingEvidence3PriorUndisputedTransactionsItem handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    charge: str = pydantic.Field(
        alias="charge",
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
    product_description: typing.Optional[typing.Union[str, str]] = pydantic.Field(
        alias="product_description", default=None
    )
    shipping_address: typing.Optional[
        _SerializerDisputeUpdateBodyEvidenceEnhancedEvidenceObj0VisaCompellingEvidence3PriorUndisputedTransactionsItemShippingAddress
    ] = pydantic.Field(alias="shipping_address", default=None)
