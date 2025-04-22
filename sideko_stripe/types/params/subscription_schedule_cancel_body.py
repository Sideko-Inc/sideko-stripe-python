import pydantic
import typing
import typing_extensions


class SubscriptionScheduleCancelBody(typing_extensions.TypedDict, total=False):
    """
    SubscriptionScheduleCancelBody
    """

    expand: typing_extensions.NotRequired[typing.List[str]]
    """
    Specifies which fields in the response should be expanded.
    """

    invoice_now: typing_extensions.NotRequired[bool]
    """
    If the subscription schedule is `active`, indicates if a final invoice will be generated that contains any un-invoiced metered usage and new/pending proration invoice items. Defaults to `true`.
    """

    prorate: typing_extensions.NotRequired[bool]
    """
    If the subscription schedule is `active`, indicates if the cancellation should be prorated. Defaults to `true`.
    """


class _SerializerSubscriptionScheduleCancelBody(pydantic.BaseModel):
    """
    Serializer for SubscriptionScheduleCancelBody handling case conversions
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
    invoice_now: typing.Optional[bool] = pydantic.Field(
        alias="invoice_now", default=None
    )
    prorate: typing.Optional[bool] = pydantic.Field(alias="prorate", default=None)
