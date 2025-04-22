import pydantic
import typing
import typing_extensions


class PaymentPagesCheckoutSessionSavedPaymentMethodOptions(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    allow_redisplay_filters: typing.Optional[
        typing.List[typing_extensions.Literal["always", "limited", "unspecified"]]
    ] = pydantic.Field(alias="allow_redisplay_filters", default=None)
    """
    Uses the `allow_redisplay` value of each saved payment method to filter the set presented to a returning customer. By default, only saved payment methods with ’allow_redisplay: ‘always’ are shown in Checkout.
    """
    payment_method_remove: typing.Optional[
        typing_extensions.Literal["disabled", "enabled"]
    ] = pydantic.Field(alias="payment_method_remove", default=None)
    """
    Enable customers to choose if they wish to remove their saved payment methods. Disabled by default.
    """
    payment_method_save: typing.Optional[
        typing_extensions.Literal["disabled", "enabled"]
    ] = pydantic.Field(alias="payment_method_save", default=None)
    """
    Enable customers to choose if they wish to save their payment method for future use. Disabled by default.
    """
