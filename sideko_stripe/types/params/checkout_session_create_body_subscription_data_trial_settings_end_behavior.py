import pydantic
import typing_extensions


class CheckoutSessionCreateBodySubscriptionDataTrialSettingsEndBehavior(
    typing_extensions.TypedDict
):
    """
    CheckoutSessionCreateBodySubscriptionDataTrialSettingsEndBehavior
    """

    missing_payment_method: typing_extensions.Required[
        typing_extensions.Literal["cancel", "create_invoice", "pause"]
    ]


class _SerializerCheckoutSessionCreateBodySubscriptionDataTrialSettingsEndBehavior(
    pydantic.BaseModel
):
    """
    Serializer for CheckoutSessionCreateBodySubscriptionDataTrialSettingsEndBehavior handling case conversions
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
