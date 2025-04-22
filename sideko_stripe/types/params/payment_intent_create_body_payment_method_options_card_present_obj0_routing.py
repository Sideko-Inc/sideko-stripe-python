import pydantic
import typing
import typing_extensions


class PaymentIntentCreateBodyPaymentMethodOptionsCardPresentObj0Routing(
    typing_extensions.TypedDict
):
    """
    PaymentIntentCreateBodyPaymentMethodOptionsCardPresentObj0Routing
    """

    requested_priority: typing_extensions.NotRequired[
        typing_extensions.Literal["domestic", "international"]
    ]


class _SerializerPaymentIntentCreateBodyPaymentMethodOptionsCardPresentObj0Routing(
    pydantic.BaseModel
):
    """
    Serializer for PaymentIntentCreateBodyPaymentMethodOptionsCardPresentObj0Routing handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    requested_priority: typing.Optional[
        typing_extensions.Literal["domestic", "international"]
    ] = pydantic.Field(alias="requested_priority", default=None)
