import pydantic
import typing
import typing_extensions

from .address import Address
from .payment_pages_checkout_session_tax_id import PaymentPagesCheckoutSessionTaxId


class PaymentPagesCheckoutSessionCustomerDetails(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    address: typing.Optional[Address] = pydantic.Field(alias="address", default=None)
    email: typing.Optional[str] = pydantic.Field(alias="email", default=None)
    """
    The email associated with the Customer, if one exists, on the Checkout Session after a completed Checkout Session or at time of session expiry.
    Otherwise, if the customer has consented to promotional content, this value is the most recent valid email provided by the customer on the Checkout form.
    """
    name: typing.Optional[str] = pydantic.Field(alias="name", default=None)
    """
    The customer's name after a completed Checkout Session. Note: This property is populated only for sessions on or after March 30, 2022.
    """
    phone: typing.Optional[str] = pydantic.Field(alias="phone", default=None)
    """
    The customer's phone number after a completed Checkout Session.
    """
    tax_exempt: typing.Optional[
        typing_extensions.Literal["exempt", "none", "reverse"]
    ] = pydantic.Field(alias="tax_exempt", default=None)
    """
    The customer’s tax exempt status after a completed Checkout Session.
    """
    tax_ids: typing.Optional[typing.List[PaymentPagesCheckoutSessionTaxId]] = (
        pydantic.Field(alias="tax_ids", default=None)
    )
    """
    The customer’s tax IDs after a completed Checkout Session.
    """
