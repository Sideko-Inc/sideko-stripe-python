import pydantic
import typing
import typing_extensions


class PaymentIntentCancelBody(typing_extensions.TypedDict, total=False):
    """
    PaymentIntentCancelBody
    """

    cancellation_reason: typing_extensions.NotRequired[
        typing_extensions.Literal[
            "abandoned", "duplicate", "fraudulent", "requested_by_customer"
        ]
    ]
    """
    Reason for canceling this PaymentIntent. Possible values are: `duplicate`, `fraudulent`, `requested_by_customer`, or `abandoned`
    """

    expand: typing_extensions.NotRequired[typing.List[str]]
    """
    Specifies which fields in the response should be expanded.
    """


class _SerializerPaymentIntentCancelBody(pydantic.BaseModel):
    """
    Serializer for PaymentIntentCancelBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, typing.Any]

    cancellation_reason: typing.Optional[
        typing_extensions.Literal[
            "abandoned", "duplicate", "fraudulent", "requested_by_customer"
        ]
    ] = pydantic.Field(alias="cancellation_reason", default=None)
    expand: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="expand", default=None
    )
