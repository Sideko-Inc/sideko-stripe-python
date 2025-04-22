import pydantic
import typing
import typing_extensions

from .quote_create_body_subscription_data_metadata import (
    QuoteCreateBodySubscriptionDataMetadata,
    _SerializerQuoteCreateBodySubscriptionDataMetadata,
)


class QuoteCreateBodySubscriptionData(typing_extensions.TypedDict):
    """
    When creating a subscription or subscription schedule, the specified configuration data will be used. There must be at least one line item with a recurring price for a subscription or subscription schedule to be created. A subscription schedule is created if `subscription_data[effective_date]` is present and in the future, otherwise a subscription is created.
    """

    description: typing_extensions.NotRequired[str]

    effective_date: typing_extensions.NotRequired[
        typing.Union[typing_extensions.Literal["current_period_end"], int, str]
    ]

    metadata: typing_extensions.NotRequired[QuoteCreateBodySubscriptionDataMetadata]

    trial_period_days: typing_extensions.NotRequired[typing.Union[int, str]]


class _SerializerQuoteCreateBodySubscriptionData(pydantic.BaseModel):
    """
    Serializer for QuoteCreateBodySubscriptionData handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    description: typing.Optional[str] = pydantic.Field(
        alias="description", default=None
    )
    effective_date: typing.Optional[
        typing.Union[typing_extensions.Literal["current_period_end"], int, str]
    ] = pydantic.Field(alias="effective_date", default=None)
    metadata: typing.Optional[_SerializerQuoteCreateBodySubscriptionDataMetadata] = (
        pydantic.Field(alias="metadata", default=None)
    )
    trial_period_days: typing.Optional[typing.Union[int, str]] = pydantic.Field(
        alias="trial_period_days", default=None
    )
