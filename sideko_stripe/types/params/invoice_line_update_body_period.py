import pydantic
import typing_extensions


class InvoiceLineUpdateBodyPeriod(typing_extensions.TypedDict):
    """
    The period associated with this invoice item. When set to different values, the period will be rendered on the invoice. If you have [Stripe Revenue Recognition](https://stripe.com/docs/revenue-recognition) enabled, the period will be used to recognize and defer revenue. See the [Revenue Recognition documentation](https://stripe.com/docs/revenue-recognition/methodology/subscriptions-and-invoicing) for details.
    """

    end: typing_extensions.Required[int]

    start: typing_extensions.Required[int]


class _SerializerInvoiceLineUpdateBodyPeriod(pydantic.BaseModel):
    """
    Serializer for InvoiceLineUpdateBodyPeriod handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    end: int = pydantic.Field(
        alias="end",
    )
    start: int = pydantic.Field(
        alias="start",
    )
