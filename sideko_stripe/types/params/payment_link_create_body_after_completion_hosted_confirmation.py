import pydantic
import typing
import typing_extensions


class PaymentLinkCreateBodyAfterCompletionHostedConfirmation(
    typing_extensions.TypedDict
):
    """
    PaymentLinkCreateBodyAfterCompletionHostedConfirmation
    """

    custom_message: typing_extensions.NotRequired[str]


class _SerializerPaymentLinkCreateBodyAfterCompletionHostedConfirmation(
    pydantic.BaseModel
):
    """
    Serializer for PaymentLinkCreateBodyAfterCompletionHostedConfirmation handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    custom_message: typing.Optional[str] = pydantic.Field(
        alias="custom_message", default=None
    )
