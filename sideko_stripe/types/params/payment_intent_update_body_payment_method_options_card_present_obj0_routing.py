import pydantic
import typing
import typing_extensions


class PaymentIntentUpdateBodyPaymentMethodOptionsCardPresentObj0Routing(
    typing_extensions.TypedDict
):
    """
    PaymentIntentUpdateBodyPaymentMethodOptionsCardPresentObj0Routing
    """

    requested_priority: typing_extensions.NotRequired[
        typing_extensions.Literal["domestic", "international"]
    ]


class _SerializerPaymentIntentUpdateBodyPaymentMethodOptionsCardPresentObj0Routing(
    pydantic.BaseModel
):
    """
    Serializer for PaymentIntentUpdateBodyPaymentMethodOptionsCardPresentObj0Routing handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    requested_priority: typing.Optional[
        typing_extensions.Literal["domestic", "international"]
    ] = pydantic.Field(alias="requested_priority", default=None)
