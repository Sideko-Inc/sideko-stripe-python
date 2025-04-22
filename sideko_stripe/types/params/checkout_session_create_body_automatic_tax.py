import pydantic
import typing
import typing_extensions

from .checkout_session_create_body_automatic_tax_liability import (
    CheckoutSessionCreateBodyAutomaticTaxLiability,
    _SerializerCheckoutSessionCreateBodyAutomaticTaxLiability,
)


class CheckoutSessionCreateBodyAutomaticTax(typing_extensions.TypedDict):
    """
    Settings for automatic tax lookup for this session and resulting payments, invoices, and subscriptions.
    """

    enabled: typing_extensions.Required[bool]

    liability: typing_extensions.NotRequired[
        CheckoutSessionCreateBodyAutomaticTaxLiability
    ]


class _SerializerCheckoutSessionCreateBodyAutomaticTax(pydantic.BaseModel):
    """
    Serializer for CheckoutSessionCreateBodyAutomaticTax handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    enabled: bool = pydantic.Field(
        alias="enabled",
    )
    liability: typing.Optional[
        _SerializerCheckoutSessionCreateBodyAutomaticTaxLiability
    ] = pydantic.Field(alias="liability", default=None)
