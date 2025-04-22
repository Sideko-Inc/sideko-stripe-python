import pydantic
import typing
import typing_extensions

from .climate_order_update_body_beneficiary_obj0 import (
    ClimateOrderUpdateBodyBeneficiaryObj0,
    _SerializerClimateOrderUpdateBodyBeneficiaryObj0,
)
from .climate_order_update_body_metadata import (
    ClimateOrderUpdateBodyMetadata,
    _SerializerClimateOrderUpdateBodyMetadata,
)


class ClimateOrderUpdateBody(typing_extensions.TypedDict, total=False):
    """
    ClimateOrderUpdateBody
    """

    beneficiary: typing_extensions.NotRequired[
        typing.Union[ClimateOrderUpdateBodyBeneficiaryObj0, str]
    ]
    """
    Publicly sharable reference for the end beneficiary of carbon removal. Assumed to be the Stripe account if not set.
    """

    expand: typing_extensions.NotRequired[typing.List[str]]
    """
    Specifies which fields in the response should be expanded.
    """

    metadata: typing_extensions.NotRequired[ClimateOrderUpdateBodyMetadata]
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    """


class _SerializerClimateOrderUpdateBody(pydantic.BaseModel):
    """
    Serializer for ClimateOrderUpdateBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, typing.Any]

    beneficiary: typing.Optional[
        typing.Union[_SerializerClimateOrderUpdateBodyBeneficiaryObj0, str]
    ] = pydantic.Field(alias="beneficiary", default=None)
    expand: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="expand", default=None
    )
    metadata: typing.Optional[_SerializerClimateOrderUpdateBodyMetadata] = (
        pydantic.Field(alias="metadata", default=None)
    )
