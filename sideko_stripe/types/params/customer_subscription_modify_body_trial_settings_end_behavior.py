import pydantic
import typing_extensions


class CustomerSubscriptionModifyBodyTrialSettingsEndBehavior(
    typing_extensions.TypedDict
):
    """
    CustomerSubscriptionModifyBodyTrialSettingsEndBehavior
    """

    missing_payment_method: typing_extensions.Required[
        typing_extensions.Literal["cancel", "create_invoice", "pause"]
    ]


class _SerializerCustomerSubscriptionModifyBodyTrialSettingsEndBehavior(
    pydantic.BaseModel
):
    """
    Serializer for CustomerSubscriptionModifyBodyTrialSettingsEndBehavior handling case conversions
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
