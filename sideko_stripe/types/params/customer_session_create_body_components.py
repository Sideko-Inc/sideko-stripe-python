import pydantic
import typing
import typing_extensions

from .customer_session_create_body_components_buy_button import (
    CustomerSessionCreateBodyComponentsBuyButton,
    _SerializerCustomerSessionCreateBodyComponentsBuyButton,
)
from .customer_session_create_body_components_payment_element import (
    CustomerSessionCreateBodyComponentsPaymentElement,
    _SerializerCustomerSessionCreateBodyComponentsPaymentElement,
)
from .customer_session_create_body_components_pricing_table import (
    CustomerSessionCreateBodyComponentsPricingTable,
    _SerializerCustomerSessionCreateBodyComponentsPricingTable,
)


class CustomerSessionCreateBodyComponents(typing_extensions.TypedDict):
    """
    Configuration for each component. Exactly 1 component must be enabled.
    """

    buy_button: typing_extensions.NotRequired[
        CustomerSessionCreateBodyComponentsBuyButton
    ]

    payment_element: typing_extensions.NotRequired[
        CustomerSessionCreateBodyComponentsPaymentElement
    ]

    pricing_table: typing_extensions.NotRequired[
        CustomerSessionCreateBodyComponentsPricingTable
    ]


class _SerializerCustomerSessionCreateBodyComponents(pydantic.BaseModel):
    """
    Serializer for CustomerSessionCreateBodyComponents handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    buy_button: typing.Optional[
        _SerializerCustomerSessionCreateBodyComponentsBuyButton
    ] = pydantic.Field(alias="buy_button", default=None)
    payment_element: typing.Optional[
        _SerializerCustomerSessionCreateBodyComponentsPaymentElement
    ] = pydantic.Field(alias="payment_element", default=None)
    pricing_table: typing.Optional[
        _SerializerCustomerSessionCreateBodyComponentsPricingTable
    ] = pydantic.Field(alias="pricing_table", default=None)
