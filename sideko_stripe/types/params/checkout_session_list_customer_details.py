import pydantic
import typing_extensions


class CheckoutSessionListCustomerDetails(typing_extensions.TypedDict):
    """
    Only return the Checkout Sessions for the Customer details specified.
    """

    email: typing_extensions.Required[str]


class _SerializerCheckoutSessionListCustomerDetails(pydantic.BaseModel):
    """
    Serializer for CheckoutSessionListCustomerDetails handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    email: str = pydantic.Field(
        alias="email",
    )
