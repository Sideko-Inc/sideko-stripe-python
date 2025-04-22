import pydantic
import typing
import typing_extensions


class CreditNotePreview1ShippingCost(typing_extensions.TypedDict):
    """
    When shipping_cost contains the shipping_rate from the invoice, the shipping_cost is included in the credit note.
    """

    shipping_rate: typing_extensions.NotRequired[str]


class _SerializerCreditNotePreview1ShippingCost(pydantic.BaseModel):
    """
    Serializer for CreditNotePreview1ShippingCost handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    shipping_rate: typing.Optional[str] = pydantic.Field(
        alias="shipping_rate", default=None
    )
