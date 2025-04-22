import pydantic
import typing_extensions


class BillingMeterResourceAggregationSettings(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    formula: typing_extensions.Literal["count", "last", "sum"] = pydantic.Field(
        alias="formula",
    )
    """
    Specifies how events are aggregated.
    """
