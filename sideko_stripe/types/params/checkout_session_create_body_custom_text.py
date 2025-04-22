import pydantic
import typing
import typing_extensions

from .checkout_session_create_body_custom_text_after_submit_obj0 import (
    CheckoutSessionCreateBodyCustomTextAfterSubmitObj0,
    _SerializerCheckoutSessionCreateBodyCustomTextAfterSubmitObj0,
)
from .checkout_session_create_body_custom_text_shipping_address_obj0 import (
    CheckoutSessionCreateBodyCustomTextShippingAddressObj0,
    _SerializerCheckoutSessionCreateBodyCustomTextShippingAddressObj0,
)
from .checkout_session_create_body_custom_text_submit_obj0 import (
    CheckoutSessionCreateBodyCustomTextSubmitObj0,
    _SerializerCheckoutSessionCreateBodyCustomTextSubmitObj0,
)
from .checkout_session_create_body_custom_text_terms_of_service_acceptance_obj0 import (
    CheckoutSessionCreateBodyCustomTextTermsOfServiceAcceptanceObj0,
    _SerializerCheckoutSessionCreateBodyCustomTextTermsOfServiceAcceptanceObj0,
)


class CheckoutSessionCreateBodyCustomText(typing_extensions.TypedDict):
    """
    Display additional text for your customers using custom text.
    """

    after_submit: typing_extensions.NotRequired[
        typing.Union[CheckoutSessionCreateBodyCustomTextAfterSubmitObj0, str]
    ]

    shipping_address: typing_extensions.NotRequired[
        typing.Union[CheckoutSessionCreateBodyCustomTextShippingAddressObj0, str]
    ]

    submit: typing_extensions.NotRequired[
        typing.Union[CheckoutSessionCreateBodyCustomTextSubmitObj0, str]
    ]

    terms_of_service_acceptance: typing_extensions.NotRequired[
        typing.Union[
            CheckoutSessionCreateBodyCustomTextTermsOfServiceAcceptanceObj0, str
        ]
    ]


class _SerializerCheckoutSessionCreateBodyCustomText(pydantic.BaseModel):
    """
    Serializer for CheckoutSessionCreateBodyCustomText handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    after_submit: typing.Optional[
        typing.Union[_SerializerCheckoutSessionCreateBodyCustomTextAfterSubmitObj0, str]
    ] = pydantic.Field(alias="after_submit", default=None)
    shipping_address: typing.Optional[
        typing.Union[
            _SerializerCheckoutSessionCreateBodyCustomTextShippingAddressObj0, str
        ]
    ] = pydantic.Field(alias="shipping_address", default=None)
    submit: typing.Optional[
        typing.Union[_SerializerCheckoutSessionCreateBodyCustomTextSubmitObj0, str]
    ] = pydantic.Field(alias="submit", default=None)
    terms_of_service_acceptance: typing.Optional[
        typing.Union[
            _SerializerCheckoutSessionCreateBodyCustomTextTermsOfServiceAcceptanceObj0,
            str,
        ]
    ] = pydantic.Field(alias="terms_of_service_acceptance", default=None)
