import pydantic
import typing_extensions


class SubscriptionListAutomaticTax(typing_extensions.TypedDict):
    """
    Filter subscriptions by their automatic tax settings.
    """

    enabled: typing_extensions.Required[bool]


class _SerializerSubscriptionListAutomaticTax(pydantic.BaseModel):
    """
    Serializer for SubscriptionListAutomaticTax handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    enabled: bool = pydantic.Field(
        alias="enabled",
    )
