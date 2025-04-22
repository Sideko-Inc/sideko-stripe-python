import pydantic
import typing
import typing_extensions


class InvoiceFinalizeBody(typing_extensions.TypedDict, total=False):
    """
    InvoiceFinalizeBody
    """

    auto_advance: typing_extensions.NotRequired[bool]
    """
    Controls whether Stripe performs [automatic collection](https://stripe.com/docs/invoicing/integration/automatic-advancement-collection) of the invoice. If `false`, the invoice's state doesn't automatically advance without an explicit action.
    """

    expand: typing_extensions.NotRequired[typing.List[str]]
    """
    Specifies which fields in the response should be expanded.
    """


class _SerializerInvoiceFinalizeBody(pydantic.BaseModel):
    """
    Serializer for InvoiceFinalizeBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, typing.Any]

    auto_advance: typing.Optional[bool] = pydantic.Field(
        alias="auto_advance", default=None
    )
    expand: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="expand", default=None
    )
