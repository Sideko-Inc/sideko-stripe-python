import pydantic
import typing
import typing_extensions

from .shipping_rate_delivery_estimate import ShippingRateDeliveryEstimate
from .shipping_rate_fixed_amount import ShippingRateFixedAmount
from .shipping_rate_metadata import ShippingRateMetadata
from .tax_code import TaxCode


class ShippingRate(pydantic.BaseModel):
    """
    Shipping rates describe the price of shipping presented to your customers and
    applied to a purchase. For more information, see [Charge for shipping](https://stripe.com/docs/payments/during-payment/charge-shipping).
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    active: bool = pydantic.Field(
        alias="active",
    )
    """
    Whether the shipping rate can be used for new purchases. Defaults to `true`.
    """
    created: int = pydantic.Field(
        alias="created",
    )
    """
    Time at which the object was created. Measured in seconds since the Unix epoch.
    """
    delivery_estimate: typing.Optional[ShippingRateDeliveryEstimate] = pydantic.Field(
        alias="delivery_estimate", default=None
    )
    display_name: typing.Optional[str] = pydantic.Field(
        alias="display_name", default=None
    )
    """
    The name of the shipping rate, meant to be displayable to the customer. This will appear on CheckoutSessions.
    """
    fixed_amount: typing.Optional[ShippingRateFixedAmount] = pydantic.Field(
        alias="fixed_amount", default=None
    )
    id: str = pydantic.Field(
        alias="id",
    )
    """
    Unique identifier for the object.
    """
    livemode: bool = pydantic.Field(
        alias="livemode",
    )
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    metadata: ShippingRateMetadata = pydantic.Field(
        alias="metadata",
    )
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    """
    object: typing_extensions.Literal["shipping_rate"] = pydantic.Field(
        alias="object",
    )
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    tax_behavior: typing.Optional[
        typing_extensions.Literal["exclusive", "inclusive", "unspecified"]
    ] = pydantic.Field(alias="tax_behavior", default=None)
    """
    Specifies whether the rate is considered inclusive of taxes or exclusive of taxes. One of `inclusive`, `exclusive`, or `unspecified`.
    """
    tax_code: typing.Optional[typing.Union[str, TaxCode]] = pydantic.Field(
        alias="tax_code", default=None
    )
    """
    A [tax code](https://stripe.com/docs/tax/tax-categories) ID. The Shipping tax code is `txcd_92010001`.
    """
    type_: typing_extensions.Literal["fixed_amount"] = pydantic.Field(
        alias="type",
    )
    """
    The type of calculation to use on the shipping rate.
    """
