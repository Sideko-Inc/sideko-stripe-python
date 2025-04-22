import pydantic
import typing
import typing_extensions

from .checkout_session_create_body_setup_intent_data_metadata import (
    CheckoutSessionCreateBodySetupIntentDataMetadata,
    _SerializerCheckoutSessionCreateBodySetupIntentDataMetadata,
)


class CheckoutSessionCreateBodySetupIntentData(typing_extensions.TypedDict):
    """
    A subset of parameters to be passed to SetupIntent creation for Checkout Sessions in `setup` mode.
    """

    description: typing_extensions.NotRequired[str]

    metadata: typing_extensions.NotRequired[
        CheckoutSessionCreateBodySetupIntentDataMetadata
    ]

    on_behalf_of: typing_extensions.NotRequired[str]


class _SerializerCheckoutSessionCreateBodySetupIntentData(pydantic.BaseModel):
    """
    Serializer for CheckoutSessionCreateBodySetupIntentData handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    description: typing.Optional[str] = pydantic.Field(
        alias="description", default=None
    )
    metadata: typing.Optional[
        _SerializerCheckoutSessionCreateBodySetupIntentDataMetadata
    ] = pydantic.Field(alias="metadata", default=None)
    on_behalf_of: typing.Optional[str] = pydantic.Field(
        alias="on_behalf_of", default=None
    )
