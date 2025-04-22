import pydantic
import typing
import typing_extensions


class CheckoutSessionCreateBodyCustomerUpdate(typing_extensions.TypedDict):
    """
    Controls what fields on Customer can be updated by the Checkout Session. Can only be provided when `customer` is provided.
    """

    address: typing_extensions.NotRequired[typing_extensions.Literal["auto", "never"]]

    name: typing_extensions.NotRequired[typing_extensions.Literal["auto", "never"]]

    shipping: typing_extensions.NotRequired[typing_extensions.Literal["auto", "never"]]


class _SerializerCheckoutSessionCreateBodyCustomerUpdate(pydantic.BaseModel):
    """
    Serializer for CheckoutSessionCreateBodyCustomerUpdate handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    address: typing.Optional[typing_extensions.Literal["auto", "never"]] = (
        pydantic.Field(alias="address", default=None)
    )
    name: typing.Optional[typing_extensions.Literal["auto", "never"]] = pydantic.Field(
        alias="name", default=None
    )
    shipping: typing.Optional[typing_extensions.Literal["auto", "never"]] = (
        pydantic.Field(alias="shipping", default=None)
    )
