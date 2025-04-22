import pydantic
import typing_extensions


class PaymentLinkUpdateBodyAfterCompletionRedirect(typing_extensions.TypedDict):
    """
    PaymentLinkUpdateBodyAfterCompletionRedirect
    """

    url: typing_extensions.Required[str]


class _SerializerPaymentLinkUpdateBodyAfterCompletionRedirect(pydantic.BaseModel):
    """
    Serializer for PaymentLinkUpdateBodyAfterCompletionRedirect handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    url: str = pydantic.Field(
        alias="url",
    )
