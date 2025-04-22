import pydantic
import typing
import typing_extensions

from .payment_link_create_body_custom_text_after_submit_obj0 import (
    PaymentLinkCreateBodyCustomTextAfterSubmitObj0,
    _SerializerPaymentLinkCreateBodyCustomTextAfterSubmitObj0,
)
from .payment_link_create_body_custom_text_shipping_address_obj0 import (
    PaymentLinkCreateBodyCustomTextShippingAddressObj0,
    _SerializerPaymentLinkCreateBodyCustomTextShippingAddressObj0,
)
from .payment_link_create_body_custom_text_submit_obj0 import (
    PaymentLinkCreateBodyCustomTextSubmitObj0,
    _SerializerPaymentLinkCreateBodyCustomTextSubmitObj0,
)
from .payment_link_create_body_custom_text_terms_of_service_acceptance_obj0 import (
    PaymentLinkCreateBodyCustomTextTermsOfServiceAcceptanceObj0,
    _SerializerPaymentLinkCreateBodyCustomTextTermsOfServiceAcceptanceObj0,
)


class PaymentLinkCreateBodyCustomText(typing_extensions.TypedDict):
    """
    Display additional text for your customers using custom text.
    """

    after_submit: typing_extensions.NotRequired[
        typing.Union[PaymentLinkCreateBodyCustomTextAfterSubmitObj0, str]
    ]

    shipping_address: typing_extensions.NotRequired[
        typing.Union[PaymentLinkCreateBodyCustomTextShippingAddressObj0, str]
    ]

    submit: typing_extensions.NotRequired[
        typing.Union[PaymentLinkCreateBodyCustomTextSubmitObj0, str]
    ]

    terms_of_service_acceptance: typing_extensions.NotRequired[
        typing.Union[PaymentLinkCreateBodyCustomTextTermsOfServiceAcceptanceObj0, str]
    ]


class _SerializerPaymentLinkCreateBodyCustomText(pydantic.BaseModel):
    """
    Serializer for PaymentLinkCreateBodyCustomText handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    after_submit: typing.Optional[
        typing.Union[_SerializerPaymentLinkCreateBodyCustomTextAfterSubmitObj0, str]
    ] = pydantic.Field(alias="after_submit", default=None)
    shipping_address: typing.Optional[
        typing.Union[_SerializerPaymentLinkCreateBodyCustomTextShippingAddressObj0, str]
    ] = pydantic.Field(alias="shipping_address", default=None)
    submit: typing.Optional[
        typing.Union[_SerializerPaymentLinkCreateBodyCustomTextSubmitObj0, str]
    ] = pydantic.Field(alias="submit", default=None)
    terms_of_service_acceptance: typing.Optional[
        typing.Union[
            _SerializerPaymentLinkCreateBodyCustomTextTermsOfServiceAcceptanceObj0, str
        ]
    ] = pydantic.Field(alias="terms_of_service_acceptance", default=None)
