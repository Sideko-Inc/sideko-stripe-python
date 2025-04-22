import pydantic
import typing
import typing_extensions


class BillingAlertCreateBodyUsageThresholdFiltersItem(typing_extensions.TypedDict):
    """
    BillingAlertCreateBodyUsageThresholdFiltersItem
    """

    customer: typing_extensions.NotRequired[str]

    type_: typing_extensions.Required[typing_extensions.Literal["customer"]]


class _SerializerBillingAlertCreateBodyUsageThresholdFiltersItem(pydantic.BaseModel):
    """
    Serializer for BillingAlertCreateBodyUsageThresholdFiltersItem handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    customer: typing.Optional[str] = pydantic.Field(alias="customer", default=None)
    type_: typing_extensions.Literal["customer"] = pydantic.Field(
        alias="type",
    )
