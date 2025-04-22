import pydantic
import typing
import typing_extensions

from .payment_intent_confirm_body_payment_method_options_card_present_obj0_routing import (
    PaymentIntentConfirmBodyPaymentMethodOptionsCardPresentObj0Routing,
    _SerializerPaymentIntentConfirmBodyPaymentMethodOptionsCardPresentObj0Routing,
)


class PaymentIntentConfirmBodyPaymentMethodOptionsCardPresentObj0(
    typing_extensions.TypedDict
):
    """
    PaymentIntentConfirmBodyPaymentMethodOptionsCardPresentObj0
    """

    request_extended_authorization: typing_extensions.NotRequired[bool]

    request_incremental_authorization_support: typing_extensions.NotRequired[bool]

    routing: typing_extensions.NotRequired[
        PaymentIntentConfirmBodyPaymentMethodOptionsCardPresentObj0Routing
    ]


class _SerializerPaymentIntentConfirmBodyPaymentMethodOptionsCardPresentObj0(
    pydantic.BaseModel
):
    """
    Serializer for PaymentIntentConfirmBodyPaymentMethodOptionsCardPresentObj0 handling case conversions
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
        _SerializerPaymentIntentConfirmBodyPaymentMethodOptionsCardPresentObj0Routing
    ] = pydantic.Field(alias="routing", default=None)
