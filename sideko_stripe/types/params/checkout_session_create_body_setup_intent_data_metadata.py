import pydantic
import typing
import typing_extensions


class CheckoutSessionCreateBodySetupIntentDataMetadata(
    typing_extensions.TypedDict, total=False
):
    """
    CheckoutSessionCreateBodySetupIntentDataMetadata
    """


class _SerializerCheckoutSessionCreateBodySetupIntentDataMetadata(pydantic.BaseModel):
    """
    Serializer for CheckoutSessionCreateBodySetupIntentDataMetadata handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, str]
