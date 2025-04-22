import pydantic
import typing
import typing_extensions

from .payment_intent_confirm_body_payment_method_options_card_obj0_installments_plan_obj0 import (
    PaymentIntentConfirmBodyPaymentMethodOptionsCardObj0InstallmentsPlanObj0,
    _SerializerPaymentIntentConfirmBodyPaymentMethodOptionsCardObj0InstallmentsPlanObj0,
)


class PaymentIntentConfirmBodyPaymentMethodOptionsCardObj0Installments(
    typing_extensions.TypedDict
):
    """
    PaymentIntentConfirmBodyPaymentMethodOptionsCardObj0Installments
    """

    enabled: typing_extensions.NotRequired[bool]

    plan: typing_extensions.NotRequired[
        typing.Union[
            PaymentIntentConfirmBodyPaymentMethodOptionsCardObj0InstallmentsPlanObj0,
            str,
        ]
    ]


class _SerializerPaymentIntentConfirmBodyPaymentMethodOptionsCardObj0Installments(
    pydantic.BaseModel
):
    """
    Serializer for PaymentIntentConfirmBodyPaymentMethodOptionsCardObj0Installments handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    enabled: typing.Optional[bool] = pydantic.Field(alias="enabled", default=None)
    plan: typing.Optional[
        typing.Union[
            _SerializerPaymentIntentConfirmBodyPaymentMethodOptionsCardObj0InstallmentsPlanObj0,
            str,
        ]
    ] = pydantic.Field(alias="plan", default=None)
