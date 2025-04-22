import pydantic
import typing
import typing_extensions

from .payment_intent_create_body_payment_method_options_card_obj0_installments_plan_obj0 import (
    PaymentIntentCreateBodyPaymentMethodOptionsCardObj0InstallmentsPlanObj0,
    _SerializerPaymentIntentCreateBodyPaymentMethodOptionsCardObj0InstallmentsPlanObj0,
)


class PaymentIntentCreateBodyPaymentMethodOptionsCardObj0Installments(
    typing_extensions.TypedDict
):
    """
    PaymentIntentCreateBodyPaymentMethodOptionsCardObj0Installments
    """

    enabled: typing_extensions.NotRequired[bool]

    plan: typing_extensions.NotRequired[
        typing.Union[
            PaymentIntentCreateBodyPaymentMethodOptionsCardObj0InstallmentsPlanObj0, str
        ]
    ]


class _SerializerPaymentIntentCreateBodyPaymentMethodOptionsCardObj0Installments(
    pydantic.BaseModel
):
    """
    Serializer for PaymentIntentCreateBodyPaymentMethodOptionsCardObj0Installments handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    enabled: typing.Optional[bool] = pydantic.Field(alias="enabled", default=None)
    plan: typing.Optional[
        typing.Union[
            _SerializerPaymentIntentCreateBodyPaymentMethodOptionsCardObj0InstallmentsPlanObj0,
            str,
        ]
    ] = pydantic.Field(alias="plan", default=None)
