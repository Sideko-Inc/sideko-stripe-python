import pydantic
import typing
import typing_extensions


class PaymentIntentCreateBodyAutomaticPaymentMethods(typing_extensions.TypedDict):
    """
    When you enable this parameter, this PaymentIntent accepts payment methods that you enable in the Dashboard and that are compatible with this PaymentIntent's other parameters.
    """

    allow_redirects: typing_extensions.NotRequired[
        typing_extensions.Literal["always", "never"]
    ]

    enabled: typing_extensions.Required[bool]


class _SerializerPaymentIntentCreateBodyAutomaticPaymentMethods(pydantic.BaseModel):
    """
    Serializer for PaymentIntentCreateBodyAutomaticPaymentMethods handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    allow_redirects: typing.Optional[typing_extensions.Literal["always", "never"]] = (
        pydantic.Field(alias="allow_redirects", default=None)
    )
    enabled: bool = pydantic.Field(
        alias="enabled",
    )
