import pydantic
import typing
import typing_extensions


class CustomerSubscriptionCreateBodyTransferData(typing_extensions.TypedDict):
    """
    If specified, the funds from the subscription's invoices will be transferred to the destination and the ID of the resulting transfers will be found on the resulting charges.
    """

    amount_percent: typing_extensions.NotRequired[float]

    destination: typing_extensions.Required[str]


class _SerializerCustomerSubscriptionCreateBodyTransferData(pydantic.BaseModel):
    """
    Serializer for CustomerSubscriptionCreateBodyTransferData handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    amount_percent: typing.Optional[float] = pydantic.Field(
        alias="amount_percent", default=None
    )
    destination: str = pydantic.Field(
        alias="destination",
    )
