import pydantic
import typing_extensions

from .issuing_cardholder_update_body_billing_address import (
    IssuingCardholderUpdateBodyBillingAddress,
    _SerializerIssuingCardholderUpdateBodyBillingAddress,
)


class IssuingCardholderUpdateBodyBilling(typing_extensions.TypedDict):
    """
    The cardholder's billing address.
    """

    address: typing_extensions.Required[IssuingCardholderUpdateBodyBillingAddress]


class _SerializerIssuingCardholderUpdateBodyBilling(pydantic.BaseModel):
    """
    Serializer for IssuingCardholderUpdateBodyBilling handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    address: _SerializerIssuingCardholderUpdateBodyBillingAddress = pydantic.Field(
        alias="address",
    )
