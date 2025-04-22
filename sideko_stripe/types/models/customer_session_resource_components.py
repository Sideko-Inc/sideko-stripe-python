import pydantic

from .customer_session_resource_components_resource_buy_button import (
    CustomerSessionResourceComponentsResourceBuyButton,
)
from .customer_session_resource_components_resource_payment_element import (
    CustomerSessionResourceComponentsResourcePaymentElement,
)
from .customer_session_resource_components_resource_pricing_table import (
    CustomerSessionResourceComponentsResourcePricingTable,
)


class CustomerSessionResourceComponents(pydantic.BaseModel):
    """
    Configuration for the components supported by this Customer Session.
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    buy_button: CustomerSessionResourceComponentsResourceBuyButton = pydantic.Field(
        alias="buy_button",
    )
    """
    This hash contains whether the buy button is enabled.
    """
    payment_element: CustomerSessionResourceComponentsResourcePaymentElement = (
        pydantic.Field(
            alias="payment_element",
        )
    )
    """
    This hash contains whether the Payment Element is enabled and the features it supports.
    """
    pricing_table: CustomerSessionResourceComponentsResourcePricingTable = (
        pydantic.Field(
            alias="pricing_table",
        )
    )
    """
    This hash contains whether the pricing table is enabled.
    """
