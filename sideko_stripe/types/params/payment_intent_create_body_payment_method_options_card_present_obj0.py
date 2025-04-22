import pydantic
import typing
import typing_extensions

from .payment_intent_create_body_payment_method_options_card_present_obj0_routing import (
    PaymentIntentCreateBodyPaymentMethodOptionsCardPresentObj0Routing,
    _SerializerPaymentIntentCreateBodyPaymentMethodOptionsCardPresentObj0Routing,
)


class PaymentIntentCreateBodyPaymentMethodOptionsCardPresentObj0(
    typing_extensions.TypedDict
):
    """
    PaymentIntentCreateBodyPaymentMethodOptionsCardPresentObj0
    """

    request_extended_authorization: typing_extensions.NotRequired[bool]

    request_incremental_authorization_support: typing_extensions.NotRequired[bool]

    routing: typing_extensions.NotRequired[
        PaymentIntentCreateBodyPaymentMethodOptionsCardPresentObj0Routing
    ]


class _SerializerPaymentIntentCreateBodyPaymentMethodOptionsCardPresentObj0(
    pydantic.BaseModel
):
    """
    Serializer for PaymentIntentCreateBodyPaymentMethodOptionsCardPresentObj0 handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    request_extended_authorization: typing.Optional[bool] = pydantic.Field(
        alias="request_extended_authorization", default=None
    )
    request_incremental_authorization_support: typing.Optional[bool] = pydantic.Field(
        alias="request_incremental_authorization_support", default=None
    )
    routing: typing.Optional[
        _SerializerPaymentIntentCreateBodyPaymentMethodOptionsCardPresentObj0Routing
    ] = pydantic.Field(alias="routing", default=None)
