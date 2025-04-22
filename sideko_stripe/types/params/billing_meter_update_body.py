import pydantic
import typing
import typing_extensions


class BillingMeterUpdateBody(typing_extensions.TypedDict, total=False):
    """
    BillingMeterUpdateBody
    """

    display_name: typing_extensions.NotRequired[str]
    """
    The meter’s name. Not visible to the customer.
    """

    expand: typing_extensions.NotRequired[typing.List[str]]
    """
    Specifies which fields in the response should be expanded.
    """


class _SerializerBillingMeterUpdateBody(pydantic.BaseModel):
    """
    Serializer for BillingMeterUpdateBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, typing.Any]

    display_name: typing.Optional[str] = pydantic.Field(
        alias="display_name", default=None
    )
    expand: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="expand", default=None
    )
