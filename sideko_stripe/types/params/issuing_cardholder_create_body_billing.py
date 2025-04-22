import pydantic
import typing_extensions

from .issuing_cardholder_create_body_billing_address import (
    IssuingCardholderCreateBodyBillingAddress,
    _SerializerIssuingCardholderCreateBodyBillingAddress,
)


class IssuingCardholderCreateBodyBilling(typing_extensions.TypedDict):
    """
    The cardholder's billing address.
    """

    address: typing_extensions.Required[IssuingCardholderCreateBodyBillingAddress]


class _SerializerIssuingCardholderCreateBodyBilling(pydantic.BaseModel):
    """
    Serializer for IssuingCardholderCreateBodyBilling handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    address: _SerializerIssuingCardholderCreateBodyBillingAddress = pydantic.Field(
        alias="address",
    )
