import pydantic
import typing
import typing_extensions

from .checkout_session_update_body_collected_information import (
    CheckoutSessionUpdateBodyCollectedInformation,
    _SerializerCheckoutSessionUpdateBodyCollectedInformation,
)
from .checkout_session_update_body_metadata_obj0 import (
    CheckoutSessionUpdateBodyMetadataObj0,
    _SerializerCheckoutSessionUpdateBodyMetadataObj0,
)
from .checkout_session_update_body_shipping_options_arr0_item import (
    CheckoutSessionUpdateBodyShippingOptionsArr0Item,
    _SerializerCheckoutSessionUpdateBodyShippingOptionsArr0Item,
)


class CheckoutSessionUpdateBody(typing_extensions.TypedDict, total=False):
    """
    CheckoutSessionUpdateBody
    """

    collected_information: typing_extensions.NotRequired[
        CheckoutSessionUpdateBodyCollectedInformation
    ]
    """
    Information about the customer collected within the Checkout Session.
    """

    expand: typing_extensions.NotRequired[typing.List[str]]
    """
    Specifies which fields in the response should be expanded.
    """

    metadata: typing_extensions.NotRequired[
        typing.Union[CheckoutSessionUpdateBodyMetadataObj0, str]
    ]
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    """

    shipping_options: typing_extensions.NotRequired[
        typing.Union[typing.List[CheckoutSessionUpdateBodyShippingOptionsArr0Item], str]
    ]
    """
    The shipping rate options to apply to this Session. Up to a maximum of 5.
    """


class _SerializerCheckoutSessionUpdateBody(pydantic.BaseModel):
    """
    Serializer for CheckoutSessionUpdateBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, typing.Any]

    collected_information: typing.Optional[
        _SerializerCheckoutSessionUpdateBodyCollectedInformation
    ] = pydantic.Field(alias="collected_information", default=None)
    expand: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="expand", default=None
    )
    metadata: typing.Optional[
        typing.Union[_SerializerCheckoutSessionUpdateBodyMetadataObj0, str]
    ] = pydantic.Field(alias="metadata", default=None)
    shipping_options: typing.Optional[
        typing.Union[
            typing.List[_SerializerCheckoutSessionUpdateBodyShippingOptionsArr0Item],
            str,
        ]
    ] = pydantic.Field(alias="shipping_options", default=None)
