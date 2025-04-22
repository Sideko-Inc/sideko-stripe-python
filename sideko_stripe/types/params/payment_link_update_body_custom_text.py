import pydantic
import typing
import typing_extensions

from .payment_link_update_body_custom_text_after_submit_obj0 import (
    PaymentLinkUpdateBodyCustomTextAfterSubmitObj0,
    _SerializerPaymentLinkUpdateBodyCustomTextAfterSubmitObj0,
)
from .payment_link_update_body_custom_text_shipping_address_obj0 import (
    PaymentLinkUpdateBodyCustomTextShippingAddressObj0,
    _SerializerPaymentLinkUpdateBodyCustomTextShippingAddressObj0,
)
from .payment_link_update_body_custom_text_submit_obj0 import (
    PaymentLinkUpdateBodyCustomTextSubmitObj0,
    _SerializerPaymentLinkUpdateBodyCustomTextSubmitObj0,
)
from .payment_link_update_body_custom_text_terms_of_service_acceptance_obj0 import (
    PaymentLinkUpdateBodyCustomTextTermsOfServiceAcceptanceObj0,
    _SerializerPaymentLinkUpdateBodyCustomTextTermsOfServiceAcceptanceObj0,
)


class PaymentLinkUpdateBodyCustomText(typing_extensions.TypedDict):
    """
    Display additional text for your customers using custom text.
    """

    after_submit: typing_extensions.NotRequired[
        typing.Union[PaymentLinkUpdateBodyCustomTextAfterSubmitObj0, str]
    ]

    shipping_address: typing_extensions.NotRequired[
        typing.Union[PaymentLinkUpdateBodyCustomTextShippingAddressObj0, str]
    ]

    submit: typing_extensions.NotRequired[
        typing.Union[PaymentLinkUpdateBodyCustomTextSubmitObj0, str]
    ]

    terms_of_service_acceptance: typing_extensions.NotRequired[
        typing.Union[PaymentLinkUpdateBodyCustomTextTermsOfServiceAcceptanceObj0, str]
    ]


class _SerializerPaymentLinkUpdateBodyCustomText(pydantic.BaseModel):
    """
    Serializer for PaymentLinkUpdateBodyCustomText handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    after_submit: typing.Optional[
        typing.Union[_SerializerPaymentLinkUpdateBodyCustomTextAfterSubmitObj0, str]
    ] = pydantic.Field(alias="after_submit", default=None)
    shipping_address: typing.Optional[
        typing.Union[_SerializerPaymentLinkUpdateBodyCustomTextShippingAddressObj0, str]
    ] = pydantic.Field(alias="shipping_address", default=None)
    submit: typing.Optional[
        typing.Union[_SerializerPaymentLinkUpdateBodyCustomTextSubmitObj0, str]
    ] = pydantic.Field(alias="submit", default=None)
    terms_of_service_acceptance: typing.Optional[
        typing.Union[
            _SerializerPaymentLinkUpdateBodyCustomTextTermsOfServiceAcceptanceObj0, str
        ]
    ] = pydantic.Field(alias="terms_of_service_acceptance", default=None)
