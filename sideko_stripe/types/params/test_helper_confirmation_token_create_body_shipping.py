import pydantic
import typing
import typing_extensions

from .test_helper_confirmation_token_create_body_shipping_address import (
    TestHelperConfirmationTokenCreateBodyShippingAddress,
    _SerializerTestHelperConfirmationTokenCreateBodyShippingAddress,
)


class TestHelperConfirmationTokenCreateBodyShipping(typing_extensions.TypedDict):
    """
    Shipping information for this ConfirmationToken.
    """

    address: typing_extensions.Required[
        TestHelperConfirmationTokenCreateBodyShippingAddress
    ]

    name: typing_extensions.Required[str]

    phone: typing_extensions.NotRequired[typing.Union[str, str]]


class _SerializerTestHelperConfirmationTokenCreateBodyShipping(pydantic.BaseModel):
    """
    Serializer for TestHelperConfirmationTokenCreateBodyShipping handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    address: _SerializerTestHelperConfirmationTokenCreateBodyShippingAddress = (
        pydantic.Field(
            alias="address",
        )
    )
    name: str = pydantic.Field(
        alias="name",
    )
    phone: typing.Optional[typing.Union[str, str]] = pydantic.Field(
        alias="phone", default=None
    )
