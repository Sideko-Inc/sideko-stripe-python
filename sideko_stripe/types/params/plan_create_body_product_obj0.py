import pydantic
import typing
import typing_extensions

from .plan_create_body_product_obj0_metadata import (
    PlanCreateBodyProductObj0Metadata,
    _SerializerPlanCreateBodyProductObj0Metadata,
)


class PlanCreateBodyProductObj0(typing_extensions.TypedDict):
    """
    The product whose pricing the created plan will represent. This can either be the ID of an existing product, or a dictionary containing fields used to create a [service product](https://stripe.com/docs/api#product_object-type).
    """

    active: typing_extensions.NotRequired[bool]

    id: typing_extensions.NotRequired[str]

    metadata: typing_extensions.NotRequired[PlanCreateBodyProductObj0Metadata]

    name: typing_extensions.Required[str]

    statement_descriptor: typing_extensions.NotRequired[str]

    tax_code: typing_extensions.NotRequired[str]

    unit_label: typing_extensions.NotRequired[str]


class _SerializerPlanCreateBodyProductObj0(pydantic.BaseModel):
    """
    Serializer for PlanCreateBodyProductObj0 handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    active: typing.Optional[bool] = pydantic.Field(alias="active", default=None)
    id: typing.Optional[str] = pydantic.Field(alias="id", default=None)
    metadata: typing.Optional[_SerializerPlanCreateBodyProductObj0Metadata] = (
        pydantic.Field(alias="metadata", default=None)
    )
    name: str = pydantic.Field(
        alias="name",
    )
    statement_descriptor: typing.Optional[str] = pydantic.Field(
        alias="statement_descriptor", default=None
    )
    tax_code: typing.Optional[str] = pydantic.Field(alias="tax_code", default=None)
    unit_label: typing.Optional[str] = pydantic.Field(alias="unit_label", default=None)
