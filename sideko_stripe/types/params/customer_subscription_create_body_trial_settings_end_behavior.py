import pydantic
import typing_extensions


class CustomerSubscriptionCreateBodyTrialSettingsEndBehavior(
    typing_extensions.TypedDict
):
    """
    CustomerSubscriptionCreateBodyTrialSettingsEndBehavior
    """

    missing_payment_method: typing_extensions.Required[
        typing_extensions.Literal["cancel", "create_invoice", "pause"]
    ]


class _SerializerCustomerSubscriptionCreateBodyTrialSettingsEndBehavior(
    pydantic.BaseModel
):
    """
    Serializer for CustomerSubscriptionCreateBodyTrialSettingsEndBehavior handling case conversions
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
