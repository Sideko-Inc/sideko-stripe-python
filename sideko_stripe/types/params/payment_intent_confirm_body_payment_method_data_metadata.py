import pydantic
import typing
import typing_extensions


class PaymentIntentConfirmBodyPaymentMethodDataMetadata(
    typing_extensions.TypedDict, total=False
):
    """
    PaymentIntentConfirmBodyPaymentMethodDataMetadata
    """


class _SerializerPaymentIntentConfirmBodyPaymentMethodDataMetadata(pydantic.BaseModel):
    """
    Serializer for PaymentIntentConfirmBodyPaymentMethodDataMetadata handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, str]
