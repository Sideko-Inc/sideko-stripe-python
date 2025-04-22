import pydantic
import typing
import typing_extensions


class CheckoutSessionCreateBodyPermissions(typing_extensions.TypedDict):
    """
    This property is used to set up permissions for various actions (e.g., update) on the CheckoutSession object.

    For specific permissions, please refer to their dedicated subsections, such as `permissions.update.shipping_details`.
    """

    update_shipping_details: typing_extensions.NotRequired[
        typing_extensions.Literal["client_only", "server_only"]
    ]


class _SerializerCheckoutSessionCreateBodyPermissions(pydantic.BaseModel):
    """
    Serializer for CheckoutSessionCreateBodyPermissions handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    update_shipping_details: typing.Optional[
        typing_extensions.Literal["client_only", "server_only"]
    ] = pydantic.Field(alias="update_shipping_details", default=None)
