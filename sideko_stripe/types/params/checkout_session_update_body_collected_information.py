import pydantic
import typing
import typing_extensions

from .checkout_session_update_body_collected_information_shipping_details import (
    CheckoutSessionUpdateBodyCollectedInformationShippingDetails,
    _SerializerCheckoutSessionUpdateBodyCollectedInformationShippingDetails,
)


class CheckoutSessionUpdateBodyCollectedInformation(typing_extensions.TypedDict):
    """
    Information about the customer collected within the Checkout Session.
    """

    shipping_details: typing_extensions.NotRequired[
        CheckoutSessionUpdateBodyCollectedInformationShippingDetails
    ]


class _SerializerCheckoutSessionUpdateBodyCollectedInformation(pydantic.BaseModel):
    """
    Serializer for CheckoutSessionUpdateBodyCollectedInformation handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    shipping_details: typing.Optional[
        _SerializerCheckoutSessionUpdateBodyCollectedInformationShippingDetails
    ] = pydantic.Field(alias="shipping_details", default=None)
