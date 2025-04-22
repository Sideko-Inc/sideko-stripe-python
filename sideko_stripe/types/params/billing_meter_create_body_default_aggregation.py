import pydantic
import typing_extensions


class BillingMeterCreateBodyDefaultAggregation(typing_extensions.TypedDict):
    """
    The default settings to aggregate a meter's events with.
    """

    formula: typing_extensions.Required[
        typing_extensions.Literal["count", "last", "sum"]
    ]


class _SerializerBillingMeterCreateBodyDefaultAggregation(pydantic.BaseModel):
    """
    Serializer for BillingMeterCreateBodyDefaultAggregation handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    formula: typing_extensions.Literal["count", "last", "sum"] = pydantic.Field(
        alias="formula",
    )
