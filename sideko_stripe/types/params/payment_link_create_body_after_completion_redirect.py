import pydantic
import typing_extensions


class PaymentLinkCreateBodyAfterCompletionRedirect(typing_extensions.TypedDict):
    """
    PaymentLinkCreateBodyAfterCompletionRedirect
    """

    url: typing_extensions.Required[str]


class _SerializerPaymentLinkCreateBodyAfterCompletionRedirect(pydantic.BaseModel):
    """
    Serializer for PaymentLinkCreateBodyAfterCompletionRedirect handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    url: str = pydantic.Field(
        alias="url",
    )
