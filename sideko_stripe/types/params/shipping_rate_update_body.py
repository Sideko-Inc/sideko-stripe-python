import pydantic
import typing
import typing_extensions

from .shipping_rate_update_body_fixed_amount import (
    ShippingRateUpdateBodyFixedAmount,
    _SerializerShippingRateUpdateBodyFixedAmount,
)
from .shipping_rate_update_body_metadata_obj0 import (
    ShippingRateUpdateBodyMetadataObj0,
    _SerializerShippingRateUpdateBodyMetadataObj0,
)


class ShippingRateUpdateBody(typing_extensions.TypedDict, total=False):
    """
    ShippingRateUpdateBody
    """

    active: typing_extensions.NotRequired[bool]
    """
    Whether the shipping rate can be used for new purchases. Defaults to `true`.
    """

    expand: typing_extensions.NotRequired[typing.List[str]]
    """
    Specifies which fields in the response should be expanded.
    """

    fixed_amount: typing_extensions.NotRequired[ShippingRateUpdateBodyFixedAmount]
    """
    Describes a fixed amount to charge for shipping. Must be present if type is `fixed_amount`.
    """

    metadata: typing_extensions.NotRequired[
        typing.Union[ShippingRateUpdateBodyMetadataObj0, str]
    ]
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    """

    tax_behavior: typing_extensions.NotRequired[
        typing_extensions.Literal["exclusive", "inclusive", "unspecified"]
    ]
    """
    Specifies whether the rate is considered inclusive of taxes or exclusive of taxes. One of `inclusive`, `exclusive`, or `unspecified`.
    """


class _SerializerShippingRateUpdateBody(pydantic.BaseModel):
    """
    Serializer for ShippingRateUpdateBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, typing.Any]

    active: typing.Optional[bool] = pydantic.Field(alias="active", default=None)
    expand: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="expand", default=None
    )
    fixed_amount: typing.Optional[_SerializerShippingRateUpdateBodyFixedAmount] = (
        pydantic.Field(alias="fixed_amount", default=None)
    )
    metadata: typing.Optional[
        typing.Union[_SerializerShippingRateUpdateBodyMetadataObj0, str]
    ] = pydantic.Field(alias="metadata", default=None)
    tax_behavior: typing.Optional[
        typing_extensions.Literal["exclusive", "inclusive", "unspecified"]
    ] = pydantic.Field(alias="tax_behavior", default=None)
