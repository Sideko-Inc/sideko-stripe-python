import pydantic
import typing
import typing_extensions

from .customer_tax_location import CustomerTaxLocation


class CustomerTax(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    automatic_tax: typing_extensions.Literal[
        "failed", "not_collecting", "supported", "unrecognized_location"
    ] = pydantic.Field(
        alias="automatic_tax",
    )
    """
    Surfaces if automatic tax computation is possible given the current customer location information.
    """
    ip_address: typing.Optional[str] = pydantic.Field(alias="ip_address", default=None)
    """
    A recent IP address of the customer used for tax reporting and tax location inference.
    """
    location: typing.Optional[CustomerTaxLocation] = pydantic.Field(
        alias="location", default=None
    )
