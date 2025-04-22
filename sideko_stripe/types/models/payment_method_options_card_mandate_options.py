import pydantic
import typing
import typing_extensions


class PaymentMethodOptionsCardMandateOptions(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    amount: int = pydantic.Field(
        alias="amount",
    )
    """
    Amount to be charged for future payments.
    """
    amount_type: typing_extensions.Literal["fixed", "maximum"] = pydantic.Field(
        alias="amount_type",
    )
    """
    One of `fixed` or `maximum`. If `fixed`, the `amount` param refers to the exact amount to be charged in future payments. If `maximum`, the amount charged can be up to the value passed for the `amount` param.
    """
    description: typing.Optional[str] = pydantic.Field(
        alias="description", default=None
    )
    """
    A description of the mandate or subscription that is meant to be displayed to the customer.
    """
    end_date: typing.Optional[int] = pydantic.Field(alias="end_date", default=None)
    """
    End date of the mandate or subscription. If not provided, the mandate will be active until canceled. If provided, end date should be after start date.
    """
    interval: typing_extensions.Literal["day", "month", "sporadic", "week", "year"] = (
        pydantic.Field(
            alias="interval",
        )
    )
    """
    Specifies payment frequency. One of `day`, `week`, `month`, `year`, or `sporadic`.
    """
    interval_count: typing.Optional[int] = pydantic.Field(
        alias="interval_count", default=None
    )
    """
    The number of intervals between payments. For example, `interval=month` and `interval_count=3` indicates one payment every three months. Maximum of one year interval allowed (1 year, 12 months, or 52 weeks). This parameter is optional when `interval=sporadic`.
    """
    reference: str = pydantic.Field(
        alias="reference",
    )
    """
    Unique identifier for the mandate or subscription.
    """
    start_date: int = pydantic.Field(
        alias="start_date",
    )
    """
    Start date of the mandate or subscription. Start date should not be lesser than yesterday.
    """
    supported_types: typing.Optional[
        typing.List[typing_extensions.Literal["india"]]
    ] = pydantic.Field(alias="supported_types", default=None)
    """
    Specifies the type of mandates supported. Possible values are `india`.
    """
