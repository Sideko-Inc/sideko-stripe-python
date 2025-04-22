import pydantic
import typing
import typing_extensions

from .dispute_transaction_shipping_address import DisputeTransactionShippingAddress


class DisputeVisaCompellingEvidence3DisputedTransaction(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    customer_account_id: typing.Optional[str] = pydantic.Field(
        alias="customer_account_id", default=None
    )
    """
    User Account ID used to log into business platform. Must be recognizable by the user.
    """
    customer_device_fingerprint: typing.Optional[str] = pydantic.Field(
        alias="customer_device_fingerprint", default=None
    )
    """
    Unique identifier of the cardholder’s device derived from a combination of at least two hardware and software attributes. Must be at least 20 characters.
    """
    customer_device_id: typing.Optional[str] = pydantic.Field(
        alias="customer_device_id", default=None
    )
    """
    Unique identifier of the cardholder’s device such as a device serial number (e.g., International Mobile Equipment Identity [IMEI]). Must be at least 15 characters.
    """
    customer_email_address: typing.Optional[str] = pydantic.Field(
        alias="customer_email_address", default=None
    )
    """
    The email address of the customer.
    """
    customer_purchase_ip: typing.Optional[str] = pydantic.Field(
        alias="customer_purchase_ip", default=None
    )
    """
    The IP address that the customer used when making the purchase.
    """
    merchandise_or_services: typing.Optional[
        typing_extensions.Literal["merchandise", "services"]
    ] = pydantic.Field(alias="merchandise_or_services", default=None)
    """
    Categorization of disputed payment.
    """
    product_description: typing.Optional[str] = pydantic.Field(
        alias="product_description", default=None
    )
    """
    A description of the product or service that was sold.
    """
    shipping_address: typing.Optional[DisputeTransactionShippingAddress] = (
        pydantic.Field(alias="shipping_address", default=None)
    )
