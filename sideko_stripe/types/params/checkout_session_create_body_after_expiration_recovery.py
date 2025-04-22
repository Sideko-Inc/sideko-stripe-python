import pydantic
import typing
import typing_extensions


class CheckoutSessionCreateBodyAfterExpirationRecovery(typing_extensions.TypedDict):
    """
    CheckoutSessionCreateBodyAfterExpirationRecovery
    """

    allow_promotion_codes: typing_extensions.NotRequired[bool]

    enabled: typing_extensions.Required[bool]


class _SerializerCheckoutSessionCreateBodyAfterExpirationRecovery(pydantic.BaseModel):
    """
    Serializer for CheckoutSessionCreateBodyAfterExpirationRecovery handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    allow_promotion_codes: typing.Optional[bool] = pydantic.Field(
        alias="allow_promotion_codes", default=None
    )
    enabled: bool = pydantic.Field(
        alias="enabled",
    )
