import pydantic
import typing
import typing_extensions

from .checkout_session_update_body_shipping_options_arr0_item_shipping_rate_data_delivery_estimate import (
    CheckoutSessionUpdateBodyShippingOptionsArr0ItemShippingRateDataDeliveryEstimate,
    _SerializerCheckoutSessionUpdateBodyShippingOptionsArr0ItemShippingRateDataDeliveryEstimate,
)
from .checkout_session_update_body_shipping_options_arr0_item_shipping_rate_data_fixed_amount import (
    CheckoutSessionUpdateBodyShippingOptionsArr0ItemShippingRateDataFixedAmount,
    _SerializerCheckoutSessionUpdateBodyShippingOptionsArr0ItemShippingRateDataFixedAmount,
)
from .checkout_session_update_body_shipping_options_arr0_item_shipping_rate_data_metadata import (
    CheckoutSessionUpdateBodyShippingOptionsArr0ItemShippingRateDataMetadata,
    _SerializerCheckoutSessionUpdateBodyShippingOptionsArr0ItemShippingRateDataMetadata,
)


class CheckoutSessionUpdateBodyShippingOptionsArr0ItemShippingRateData(
    typing_extensions.TypedDict
):
    """
    CheckoutSessionUpdateBodyShippingOptionsArr0ItemShippingRateData
    """

    delivery_estimate: typing_extensions.NotRequired[
        CheckoutSessionUpdateBodyShippingOptionsArr0ItemShippingRateDataDeliveryEstimate
    ]

    display_name: typing_extensions.Required[str]

    fixed_amount: typing_extensions.NotRequired[
        CheckoutSessionUpdateBodyShippingOptionsArr0ItemShippingRateDataFixedAmount
    ]

    metadata: typing_extensions.NotRequired[
        CheckoutSessionUpdateBodyShippingOptionsArr0ItemShippingRateDataMetadata
    ]

    tax_behavior: typing_extensions.NotRequired[
        typing_extensions.Literal["exclusive", "inclusive", "unspecified"]
    ]

    tax_code: typing_extensions.NotRequired[str]

    type_: typing_extensions.NotRequired[typing_extensions.Literal["fixed_amount"]]


class _SerializerCheckoutSessionUpdateBodyShippingOptionsArr0ItemShippingRateData(
    pydantic.BaseModel
):
    """
    Serializer for CheckoutSessionUpdateBodyShippingOptionsArr0ItemShippingRateData handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    delivery_estimate: typing.Optional[
        _SerializerCheckoutSessionUpdateBodyShippingOptionsArr0ItemShippingRateDataDeliveryEstimate
    ] = pydantic.Field(alias="delivery_estimate", default=None)
    display_name: str = pydantic.Field(
        alias="display_name",
    )
    fixed_amount: typing.Optional[
        _SerializerCheckoutSessionUpdateBodyShippingOptionsArr0ItemShippingRateDataFixedAmount
    ] = pydantic.Field(alias="fixed_amount", default=None)
    metadata: typing.Optional[
        _SerializerCheckoutSessionUpdateBodyShippingOptionsArr0ItemShippingRateDataMetadata
    ] = pydantic.Field(alias="metadata", default=None)
    tax_behavior: typing.Optional[
        typing_extensions.Literal["exclusive", "inclusive", "unspecified"]
    ] = pydantic.Field(alias="tax_behavior", default=None)
    tax_code: typing.Optional[str] = pydantic.Field(alias="tax_code", default=None)
    type_: typing.Optional[typing_extensions.Literal["fixed_amount"]] = pydantic.Field(
        alias="type", default=None
    )
