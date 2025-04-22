import pydantic
import typing


class CustomUnitAmount(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    maximum: typing.Optional[int] = pydantic.Field(alias="maximum", default=None)
    """
    The maximum unit amount the customer can specify for this item.
    """
    minimum: typing.Optional[int] = pydantic.Field(alias="minimum", default=None)
    """
    The minimum unit amount the customer can specify for this item. Must be at least the minimum charge amount.
    """
    preset: typing.Optional[int] = pydantic.Field(alias="preset", default=None)
    """
    The starting unit amount which can be updated by the customer.
    """
