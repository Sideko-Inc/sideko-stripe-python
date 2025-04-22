import pydantic
import typing
import typing_extensions


class PaymentPagesCheckoutSessionPermissions(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    update_shipping_details: typing.Optional[
        typing_extensions.Literal["client_only", "server_only"]
    ] = pydantic.Field(alias="update_shipping_details", default=None)
    """
    Determines which entity is allowed to update the shipping details.
    
    Default is `client_only`. Stripe Checkout client will automatically update the shipping details. If set to `server_only`, only your server is allowed to update the shipping details.
    
    When set to `server_only`, you must add the onShippingDetailsChange event handler when initializing the Stripe Checkout client and manually update the shipping details from your server using the Stripe API.
    """
