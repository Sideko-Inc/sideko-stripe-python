import pydantic
import typing


class IssuingAuthorizationMerchantData(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    category: str = pydantic.Field(
        alias="category",
    )
    """
    A categorization of the seller's type of business. See our [merchant categories guide](https://stripe.com/docs/issuing/merchant-categories) for a list of possible values.
    """
    category_code: str = pydantic.Field(
        alias="category_code",
    )
    """
    The merchant category code for the seller’s business
    """
    city: typing.Optional[str] = pydantic.Field(alias="city", default=None)
    """
    City where the seller is located
    """
    country: typing.Optional[str] = pydantic.Field(alias="country", default=None)
    """
    Country where the seller is located
    """
    name: typing.Optional[str] = pydantic.Field(alias="name", default=None)
    """
    Name of the seller
    """
    network_id: str = pydantic.Field(
        alias="network_id",
    )
    """
    Identifier assigned to the seller by the card network. Different card networks may assign different network_id fields to the same merchant.
    """
    postal_code: typing.Optional[str] = pydantic.Field(
        alias="postal_code", default=None
    )
    """
    Postal code where the seller is located
    """
    state: typing.Optional[str] = pydantic.Field(alias="state", default=None)
    """
    State where the seller is located
    """
    tax_id: typing.Optional[str] = pydantic.Field(alias="tax_id", default=None)
    """
    The seller's tax identification number. Currently populated for French merchants only.
    """
    terminal_id: typing.Optional[str] = pydantic.Field(
        alias="terminal_id", default=None
    )
    """
    An ID assigned by the seller to the location of the sale.
    """
    url: typing.Optional[str] = pydantic.Field(alias="url", default=None)
    """
    URL provided by the merchant on a 3DS request
    """
