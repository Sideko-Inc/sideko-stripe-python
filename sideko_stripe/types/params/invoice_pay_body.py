import pydantic
import typing
import typing_extensions


class InvoicePayBody(typing_extensions.TypedDict, total=False):
    """
    InvoicePayBody
    """

    expand: typing_extensions.NotRequired[typing.List[str]]
    """
    Specifies which fields in the response should be expanded.
    """

    forgive: typing_extensions.NotRequired[bool]
    """
    In cases where the source used to pay the invoice has insufficient funds, passing `forgive=true` controls whether a charge should be attempted for the full amount available on the source, up to the amount to fully pay the invoice. This effectively forgives the difference between the amount available on the source and the amount due. 
    
    Passing `forgive=false` will fail the charge if the source hasn't been pre-funded with the right amount. An example for this case is with ACH Credit Transfers and wires: if the amount wired is less than the amount due by a small amount, you might want to forgive the difference. Defaults to `false`.
    """

    mandate: typing_extensions.NotRequired[typing.Union[str, str]]
    """
    ID of the mandate to be used for this invoice. It must correspond to the payment method used to pay the invoice, including the payment_method param or the invoice's default_payment_method or default_source, if set.
    """

    off_session: typing_extensions.NotRequired[bool]
    """
    Indicates if a customer is on or off-session while an invoice payment is attempted. Defaults to `true` (off-session).
    """

    paid_out_of_band: typing_extensions.NotRequired[bool]
    """
    Boolean representing whether an invoice is paid outside of Stripe. This will result in no charge being made. Defaults to `false`.
    """

    payment_method: typing_extensions.NotRequired[str]
    """
    A PaymentMethod to be charged. The PaymentMethod must be the ID of a PaymentMethod belonging to the customer associated with the invoice being paid.
    """

    source: typing_extensions.NotRequired[str]
    """
    A payment source to be charged. The source must be the ID of a source belonging to the customer associated with the invoice being paid.
    """


class _SerializerInvoicePayBody(pydantic.BaseModel):
    """
    Serializer for InvoicePayBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, typing.Any]

    expand: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="expand", default=None
    )
    forgive: typing.Optional[bool] = pydantic.Field(alias="forgive", default=None)
    mandate: typing.Optional[typing.Union[str, str]] = pydantic.Field(
        alias="mandate", default=None
    )
    off_session: typing.Optional[bool] = pydantic.Field(
        alias="off_session", default=None
    )
    paid_out_of_band: typing.Optional[bool] = pydantic.Field(
        alias="paid_out_of_band", default=None
    )
    payment_method: typing.Optional[str] = pydantic.Field(
        alias="payment_method", default=None
    )
    source: typing.Optional[str] = pydantic.Field(alias="source", default=None)
