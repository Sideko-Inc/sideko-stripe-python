import pydantic
import typing
import typing_extensions

from .payment_intent_update_body_payment_method_options_card_obj0_installments_plan_obj0 import (
    PaymentIntentUpdateBodyPaymentMethodOptionsCardObj0InstallmentsPlanObj0,
    _SerializerPaymentIntentUpdateBodyPaymentMethodOptionsCardObj0InstallmentsPlanObj0,
)


class PaymentIntentUpdateBodyPaymentMethodOptionsCardObj0Installments(
    typing_extensions.TypedDict
):
    """
    PaymentIntentUpdateBodyPaymentMethodOptionsCardObj0Installments
    """

    enabled: typing_extensions.NotRequired[bool]

    plan: typing_extensions.NotRequired[
        typing.Union[
            PaymentIntentUpdateBodyPaymentMethodOptionsCardObj0InstallmentsPlanObj0, str
        ]
    ]


class _SerializerPaymentIntentUpdateBodyPaymentMethodOptionsCardObj0Installments(
    pydantic.BaseModel
):
    """
    Serializer for PaymentIntentUpdateBodyPaymentMethodOptionsCardObj0Installments handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    enabled: typing.Optional[bool] = pydantic.Field(alias="enabled", default=None)
    plan: typing.Optional[
        typing.Union[
            _SerializerPaymentIntentUpdateBodyPaymentMethodOptionsCardObj0InstallmentsPlanObj0,
            str,
        ]
    ] = pydantic.Field(alias="plan", default=None)
