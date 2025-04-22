import pydantic
import typing
import typing_extensions

from .checkout_session_create_body_consent_collection_payment_method_reuse_agreement import (
    CheckoutSessionCreateBodyConsentCollectionPaymentMethodReuseAgreement,
    _SerializerCheckoutSessionCreateBodyConsentCollectionPaymentMethodReuseAgreement,
)


class CheckoutSessionCreateBodyConsentCollection(typing_extensions.TypedDict):
    """
    Configure fields for the Checkout Session to gather active consent from customers.
    """

    payment_method_reuse_agreement: typing_extensions.NotRequired[
        CheckoutSessionCreateBodyConsentCollectionPaymentMethodReuseAgreement
    ]

    promotions: typing_extensions.NotRequired[typing_extensions.Literal["auto", "none"]]

    terms_of_service: typing_extensions.NotRequired[
        typing_extensions.Literal["none", "required"]
    ]


class _SerializerCheckoutSessionCreateBodyConsentCollection(pydantic.BaseModel):
    """
    Serializer for CheckoutSessionCreateBodyConsentCollection handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    payment_method_reuse_agreement: typing.Optional[
        _SerializerCheckoutSessionCreateBodyConsentCollectionPaymentMethodReuseAgreement
    ] = pydantic.Field(alias="payment_method_reuse_agreement", default=None)
    promotions: typing.Optional[typing_extensions.Literal["auto", "none"]] = (
        pydantic.Field(alias="promotions", default=None)
    )
    terms_of_service: typing.Optional[typing_extensions.Literal["none", "required"]] = (
        pydantic.Field(alias="terms_of_service", default=None)
    )
