import pydantic
import typing
import typing_extensions

from .climate_order_metadata import ClimateOrderMetadata
from .climate_product import ClimateProduct
from .climate_removals_beneficiary import ClimateRemovalsBeneficiary
from .climate_removals_order_deliveries import ClimateRemovalsOrderDeliveries


class ClimateOrder(pydantic.BaseModel):
    """
    Orders represent your intent to purchase a particular Climate product. When you create an order, the
    payment is deducted from your merchant balance.
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    amount_fees: int = pydantic.Field(
        alias="amount_fees",
    )
    """
    Total amount of [Frontier](https://frontierclimate.com/)'s service fees in the currency's smallest unit.
    """
    amount_subtotal: int = pydantic.Field(
        alias="amount_subtotal",
    )
    """
    Total amount of the carbon removal in the currency's smallest unit.
    """
    amount_total: int = pydantic.Field(
        alias="amount_total",
    )
    """
    Total amount of the order including fees in the currency's smallest unit.
    """
    beneficiary: typing.Optional[ClimateRemovalsBeneficiary] = pydantic.Field(
        alias="beneficiary", default=None
    )
    canceled_at: typing.Optional[int] = pydantic.Field(
        alias="canceled_at", default=None
    )
    """
    Time at which the order was canceled. Measured in seconds since the Unix epoch.
    """
    cancellation_reason: typing.Optional[
        typing_extensions.Literal["expired", "product_unavailable", "requested"]
    ] = pydantic.Field(alias="cancellation_reason", default=None)
    """
    Reason for the cancellation of this order.
    """
    certificate: typing.Optional[str] = pydantic.Field(
        alias="certificate", default=None
    )
    """
    For delivered orders, a URL to a delivery certificate for the order.
    """
    confirmed_at: typing.Optional[int] = pydantic.Field(
        alias="confirmed_at", default=None
    )
    """
    Time at which the order was confirmed. Measured in seconds since the Unix epoch.
    """
    created: int = pydantic.Field(
        alias="created",
    )
    """
    Time at which the object was created. Measured in seconds since the Unix epoch.
    """
    currency: str = pydantic.Field(
        alias="currency",
    )
    """
    Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase, representing the currency for this order.
    """
    delayed_at: typing.Optional[int] = pydantic.Field(alias="delayed_at", default=None)
    """
    Time at which the order's expected_delivery_year was delayed. Measured in seconds since the Unix epoch.
    """
    delivered_at: typing.Optional[int] = pydantic.Field(
        alias="delivered_at", default=None
    )
    """
    Time at which the order was delivered. Measured in seconds since the Unix epoch.
    """
    delivery_details: typing.List[ClimateRemovalsOrderDeliveries] = pydantic.Field(
        alias="delivery_details",
    )
    """
    Details about the delivery of carbon removal for this order.
    """
    expected_delivery_year: int = pydantic.Field(
        alias="expected_delivery_year",
    )
    """
    The year this order is expected to be delivered.
    """
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
    metadata: ClimateOrderMetadata = pydantic.Field(
        alias="metadata",
    )
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    """
    metric_tons: str = pydantic.Field(
        alias="metric_tons",
    )
    """
    Quantity of carbon removal that is included in this order.
    """
    object: typing_extensions.Literal["climate.order"] = pydantic.Field(
        alias="object",
    )
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    product: typing.Union[str, ClimateProduct] = pydantic.Field(
        alias="product",
    )
    """
    Unique ID for the Climate `Product` this order is purchasing.
    """
    product_substituted_at: typing.Optional[int] = pydantic.Field(
        alias="product_substituted_at", default=None
    )
    """
    Time at which the order's product was substituted for a different product. Measured in seconds since the Unix epoch.
    """
    status: typing_extensions.Literal[
        "awaiting_funds", "canceled", "confirmed", "delivered", "open"
    ] = pydantic.Field(
        alias="status",
    )
    """
    The current status of this order.
    """
