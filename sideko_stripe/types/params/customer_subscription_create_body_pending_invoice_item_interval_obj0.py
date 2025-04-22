import pydantic
import typing
import typing_extensions


class CustomerSubscriptionCreateBodyPendingInvoiceItemIntervalObj0(
    typing_extensions.TypedDict
):
    """
    CustomerSubscriptionCreateBodyPendingInvoiceItemIntervalObj0
    """

    interval: typing_extensions.Required[
        typing_extensions.Literal["day", "month", "week", "year"]
    ]

    interval_count: typing_extensions.NotRequired[int]


class _SerializerCustomerSubscriptionCreateBodyPendingInvoiceItemIntervalObj0(
    pydantic.BaseModel
):
    """
    Serializer for CustomerSubscriptionCreateBodyPendingInvoiceItemIntervalObj0 handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    interval: typing_extensions.Literal["day", "month", "week", "year"] = (
        pydantic.Field(
            alias="interval",
        )
    )
    interval_count: typing.Optional[int] = pydantic.Field(
        alias="interval_count", default=None
    )
