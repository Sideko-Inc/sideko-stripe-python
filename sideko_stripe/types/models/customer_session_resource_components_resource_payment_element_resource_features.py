import pydantic
import typing
import typing_extensions


class CustomerSessionResourceComponentsResourcePaymentElementResourceFeatures(
    pydantic.BaseModel
):
    """
    This hash contains the features the Payment Element supports.
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    payment_method_allow_redisplay_filters: typing.List[
        typing_extensions.Literal["always", "limited", "unspecified"]
    ] = pydantic.Field(
        alias="payment_method_allow_redisplay_filters",
    )
    """
    A list of [`allow_redisplay`](https://docs.stripe.com/api/payment_methods/object#payment_method_object-allow_redisplay) values that controls which saved payment methods the Payment Element displays by filtering to only show payment methods with an `allow_redisplay` value that is present in this list.
    
    If not specified, defaults to ["always"]. In order to display all saved payment methods, specify ["always", "limited", "unspecified"].
    """
    payment_method_redisplay: typing_extensions.Literal["disabled", "enabled"] = (
        pydantic.Field(
            alias="payment_method_redisplay",
        )
    )
    """
    Controls whether or not the Payment Element shows saved payment methods. This parameter defaults to `disabled`.
    """
    payment_method_redisplay_limit: typing.Optional[int] = pydantic.Field(
        alias="payment_method_redisplay_limit", default=None
    )
    """
    Determines the max number of saved payment methods for the Payment Element to display. This parameter defaults to `3`.
    """
    payment_method_remove: typing_extensions.Literal["disabled", "enabled"] = (
        pydantic.Field(
            alias="payment_method_remove",
        )
    )
    """
    Controls whether the Payment Element displays the option to remove a saved payment method. This parameter defaults to `disabled`.
    
    Allowing buyers to remove their saved payment methods impacts subscriptions that depend on that payment method. Removing the payment method detaches the [`customer` object](https://docs.stripe.com/api/payment_methods/object#payment_method_object-customer) from that [PaymentMethod](https://docs.stripe.com/api/payment_methods).
    """
    payment_method_save: typing_extensions.Literal["disabled", "enabled"] = (
        pydantic.Field(
            alias="payment_method_save",
        )
    )
    """
    Controls whether the Payment Element displays a checkbox offering to save a new payment method. This parameter defaults to `disabled`.
    
    If a customer checks the box, the [`allow_redisplay`](https://docs.stripe.com/api/payment_methods/object#payment_method_object-allow_redisplay) value on the PaymentMethod is set to `'always'` at confirmation time. For PaymentIntents, the [`setup_future_usage`](https://docs.stripe.com/api/payment_intents/object#payment_intent_object-setup_future_usage) value is also set to the value defined in `payment_method_save_usage`.
    """
    payment_method_save_usage: typing.Optional[
        typing_extensions.Literal["off_session", "on_session"]
    ] = pydantic.Field(alias="payment_method_save_usage", default=None)
    """
    When using PaymentIntents and the customer checks the save checkbox, this field determines the [`setup_future_usage`](https://docs.stripe.com/api/payment_intents/object#payment_intent_object-setup_future_usage) value used to confirm the PaymentIntent.
    
    When using SetupIntents, directly configure the [`usage`](https://docs.stripe.com/api/setup_intents/object#setup_intent_object-usage) value on SetupIntent creation.
    """
