import pydantic
import typing_extensions

from .checkout_session_update_body_collected_information_shipping_details_address import (
    CheckoutSessionUpdateBodyCollectedInformationShippingDetailsAddress,
    _SerializerCheckoutSessionUpdateBodyCollectedInformationShippingDetailsAddress,
)


class CheckoutSessionUpdateBodyCollectedInformationShippingDetails(
    typing_extensions.TypedDict
):
    """
    CheckoutSessionUpdateBodyCollectedInformationShippingDetails
    """

    address: typing_extensions.Required[
        CheckoutSessionUpdateBodyCollectedInformationShippingDetailsAddress
    ]

    name: typing_extensions.Required[str]


class _SerializerCheckoutSessionUpdateBodyCollectedInformationShippingDetails(
    pydantic.BaseModel
):
    """
    Serializer for CheckoutSessionUpdateBodyCollectedInformationShippingDetails handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    address: _SerializerCheckoutSessionUpdateBodyCollectedInformationShippingDetailsAddress = pydantic.Field(
        alias="address",
    )
    name: str = pydantic.Field(
        alias="name",
    )
