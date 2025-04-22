import pydantic
import typing_extensions


class PaymentLinkUpdateBodySubscriptionDataTrialSettingsObj0EndBehavior(
    typing_extensions.TypedDict
):
    """
    PaymentLinkUpdateBodySubscriptionDataTrialSettingsObj0EndBehavior
    """

    missing_payment_method: typing_extensions.Required[
        typing_extensions.Literal["cancel", "create_invoice", "pause"]
    ]


class _SerializerPaymentLinkUpdateBodySubscriptionDataTrialSettingsObj0EndBehavior(
    pydantic.BaseModel
):
    """
    Serializer for PaymentLinkUpdateBodySubscriptionDataTrialSettingsObj0EndBehavior handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    missing_payment_method: typing_extensions.Literal[
        "cancel", "create_invoice", "pause"
    ] = pydantic.Field(
        alias="missing_payment_method",
    )
