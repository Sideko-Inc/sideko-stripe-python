import pydantic
import typing
import typing_extensions

from .shipping_rate_create_body_delivery_estimate import (
    ShippingRateCreateBodyDeliveryEstimate,
    _SerializerShippingRateCreateBodyDeliveryEstimate,
)
from .shipping_rate_create_body_fixed_amount import (
    ShippingRateCreateBodyFixedAmount,
    _SerializerShippingRateCreateBodyFixedAmount,
)
from .shipping_rate_create_body_metadata import (
    ShippingRateCreateBodyMetadata,
    _SerializerShippingRateCreateBodyMetadata,
)


class ShippingRateCreateBody(typing_extensions.TypedDict, total=False):
    """
    ShippingRateCreateBody
    """

    delivery_estimate: typing_extensions.NotRequired[
        ShippingRateCreateBodyDeliveryEstimate
    ]
    """
    The estimated range for how long shipping will take, meant to be displayable to the customer. This will appear on CheckoutSessions.
    """

    display_name: typing_extensions.Required[str]
    """
    The name of the shipping rate, meant to be displayable to the customer. This will appear on CheckoutSessions.
    """

    expand: typing_extensions.NotRequired[typing.List[str]]
    """
    Specifies which fields in the response should be expanded.
    """

    fixed_amount: typing_extensions.NotRequired[ShippingRateCreateBodyFixedAmount]
    """
    Describes a fixed amount to charge for shipping. Must be present if type is `fixed_amount`.
    """

    metadata: typing_extensions.NotRequired[ShippingRateCreateBodyMetadata]
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    """

    tax_behavior: typing_extensions.NotRequired[
        typing_extensions.Literal["exclusive", "inclusive", "unspecified"]
    ]
    """
    Specifies whether the rate is considered inclusive of taxes or exclusive of taxes. One of `inclusive`, `exclusive`, or `unspecified`.
    """

    tax_code: typing_extensions.NotRequired[str]
    """
    A [tax code](https://stripe.com/docs/tax/tax-categories) ID. The Shipping tax code is `txcd_92010001`.
    """

    type_: typing_extensions.NotRequired[typing_extensions.Literal["fixed_amount"]]
    """
    The type of calculation to use on the shipping rate.
    """


class _SerializerShippingRateCreateBody(pydantic.BaseModel):
    """
    Serializer for ShippingRateCreateBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, typing.Any]

    delivery_estimate: typing.Optional[
        _SerializerShippingRateCreateBodyDeliveryEstimate
    ] = pydantic.Field(alias="delivery_estimate", default=None)
    display_name: str = pydantic.Field(
        alias="display_name",
    )
    expand: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="expand", default=None
    )
    fixed_amount: typing.Optional[_SerializerShippingRateCreateBodyFixedAmount] = (
        pydantic.Field(alias="fixed_amount", default=None)
    )
    metadata: typing.Optional[_SerializerShippingRateCreateBodyMetadata] = (
        pydantic.Field(alias="metadata", default=None)
    )
    tax_behavior: typing.Optional[
        typing_extensions.Literal["exclusive", "inclusive", "unspecified"]
    ] = pydantic.Field(alias="tax_behavior", default=None)
    tax_code: typing.Optional[str] = pydantic.Field(alias="tax_code", default=None)
    type_: typing.Optional[typing_extensions.Literal["fixed_amount"]] = pydantic.Field(
        alias="type", default=None
    )
