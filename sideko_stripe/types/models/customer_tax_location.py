import pydantic
import typing
import typing_extensions


class CustomerTaxLocation(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    country: str = pydantic.Field(
        alias="country",
    )
    """
    The identified tax country of the customer.
    """
    source: typing_extensions.Literal[
        "billing_address", "ip_address", "payment_method", "shipping_destination"
    ] = pydantic.Field(
        alias="source",
    )
    """
    The data source used to infer the customer's location.
    """
    state: typing.Optional[str] = pydantic.Field(alias="state", default=None)
    """
    The identified tax state, county, province, or region of the customer.
    """
