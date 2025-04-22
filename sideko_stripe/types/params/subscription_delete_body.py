import pydantic
import typing
import typing_extensions

from .subscription_delete_body_cancellation_details import (
    SubscriptionDeleteBodyCancellationDetails,
    _SerializerSubscriptionDeleteBodyCancellationDetails,
)


class SubscriptionDeleteBody(typing_extensions.TypedDict, total=False):
    """
    SubscriptionDeleteBody
    """

    cancellation_details: typing_extensions.NotRequired[
        SubscriptionDeleteBodyCancellationDetails
    ]
    """
    Details about why this subscription was cancelled
    """

    expand: typing_extensions.NotRequired[typing.List[str]]
    """
    Specifies which fields in the response should be expanded.
    """

    invoice_now: typing_extensions.NotRequired[bool]
    """
    Will generate a final invoice that invoices for any un-invoiced metered usage and new/pending proration invoice items. Defaults to `false`.
    """

    prorate: typing_extensions.NotRequired[bool]
    """
    Will generate a proration invoice item that credits remaining unused time until the subscription period end. Defaults to `false`.
    """


class _SerializerSubscriptionDeleteBody(pydantic.BaseModel):
    """
    Serializer for SubscriptionDeleteBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, typing.Any]

    cancellation_details: typing.Optional[
        _SerializerSubscriptionDeleteBodyCancellationDetails
    ] = pydantic.Field(alias="cancellation_details", default=None)
    expand: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="expand", default=None
    )
    invoice_now: typing.Optional[bool] = pydantic.Field(
        alias="invoice_now", default=None
    )
    prorate: typing.Optional[bool] = pydantic.Field(alias="prorate", default=None)
