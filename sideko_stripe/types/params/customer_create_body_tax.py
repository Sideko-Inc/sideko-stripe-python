import pydantic
import typing
import typing_extensions


class CustomerCreateBodyTax(typing_extensions.TypedDict):
    """
    Tax details about the customer.
    """

    ip_address: typing_extensions.NotRequired[typing.Union[str, str]]

    validate_location: typing_extensions.NotRequired[
        typing_extensions.Literal["deferred", "immediately"]
    ]


class _SerializerCustomerCreateBodyTax(pydantic.BaseModel):
    """
    Serializer for CustomerCreateBodyTax handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    ip_address: typing.Optional[typing.Union[str, str]] = pydantic.Field(
        alias="ip_address", default=None
    )
    validate_location: typing.Optional[
        typing_extensions.Literal["deferred", "immediately"]
    ] = pydantic.Field(alias="validate_location", default=None)
