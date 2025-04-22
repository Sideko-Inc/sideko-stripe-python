import pydantic
import typing
import typing_extensions


class PaymentLinkUpdateBodyAfterCompletionHostedConfirmation(
    typing_extensions.TypedDict
):
    """
    PaymentLinkUpdateBodyAfterCompletionHostedConfirmation
    """

    custom_message: typing_extensions.NotRequired[str]


class _SerializerPaymentLinkUpdateBodyAfterCompletionHostedConfirmation(
    pydantic.BaseModel
):
    """
    Serializer for PaymentLinkUpdateBodyAfterCompletionHostedConfirmation handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    custom_message: typing.Optional[str] = pydantic.Field(
        alias="custom_message", default=None
    )
