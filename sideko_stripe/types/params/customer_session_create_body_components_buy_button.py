import pydantic
import typing_extensions


class CustomerSessionCreateBodyComponentsBuyButton(typing_extensions.TypedDict):
    """
    CustomerSessionCreateBodyComponentsBuyButton
    """

    enabled: typing_extensions.Required[bool]


class _SerializerCustomerSessionCreateBodyComponentsBuyButton(pydantic.BaseModel):
    """
    Serializer for CustomerSessionCreateBodyComponentsBuyButton handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    enabled: bool = pydantic.Field(
        alias="enabled",
    )
