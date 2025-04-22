import pydantic
import typing_extensions


class CustomerSessionCreateBodyComponentsPricingTable(typing_extensions.TypedDict):
    """
    CustomerSessionCreateBodyComponentsPricingTable
    """

    enabled: typing_extensions.Required[bool]


class _SerializerCustomerSessionCreateBodyComponentsPricingTable(pydantic.BaseModel):
    """
    Serializer for CustomerSessionCreateBodyComponentsPricingTable handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    enabled: bool = pydantic.Field(
        alias="enabled",
    )
