import pydantic
import typing
import typing_extensions


class SubscriptionUpdateBodyPaymentSettingsPaymentMethodOptionsAcssDebitObj0MandateOptions(
    typing_extensions.TypedDict
):
    """
    SubscriptionUpdateBodyPaymentSettingsPaymentMethodOptionsAcssDebitObj0MandateOptions
    """

    transaction_type: typing_extensions.NotRequired[
        typing_extensions.Literal["business", "personal"]
    ]


class _SerializerSubscriptionUpdateBodyPaymentSettingsPaymentMethodOptionsAcssDebitObj0MandateOptions(
    pydantic.BaseModel
):
    """
    Serializer for SubscriptionUpdateBodyPaymentSettingsPaymentMethodOptionsAcssDebitObj0MandateOptions handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    transaction_type: typing.Optional[
        typing_extensions.Literal["business", "personal"]
    ] = pydantic.Field(alias="transaction_type", default=None)
