import pydantic
import typing
import typing_extensions

from .quote_update_body_subscription_data_metadata import (
    QuoteUpdateBodySubscriptionDataMetadata,
    _SerializerQuoteUpdateBodySubscriptionDataMetadata,
)


class QuoteUpdateBodySubscriptionData(typing_extensions.TypedDict):
    """
    When creating a subscription or subscription schedule, the specified configuration data will be used. There must be at least one line item with a recurring price for a subscription or subscription schedule to be created. A subscription schedule is created if `subscription_data[effective_date]` is present and in the future, otherwise a subscription is created.
    """

    description: typing_extensions.NotRequired[typing.Union[str, str]]

    effective_date: typing_extensions.NotRequired[
        typing.Union[typing_extensions.Literal["current_period_end"], int, str]
    ]

    metadata: typing_extensions.NotRequired[QuoteUpdateBodySubscriptionDataMetadata]

    trial_period_days: typing_extensions.NotRequired[typing.Union[int, str]]


class _SerializerQuoteUpdateBodySubscriptionData(pydantic.BaseModel):
    """
    Serializer for QuoteUpdateBodySubscriptionData handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    description: typing.Optional[typing.Union[str, str]] = pydantic.Field(
        alias="description", default=None
    )
    effective_date: typing.Optional[
        typing.Union[typing_extensions.Literal["current_period_end"], int, str]
    ] = pydantic.Field(alias="effective_date", default=None)
    metadata: typing.Optional[_SerializerQuoteUpdateBodySubscriptionDataMetadata] = (
        pydantic.Field(alias="metadata", default=None)
    )
    trial_period_days: typing.Optional[typing.Union[int, str]] = pydantic.Field(
        alias="trial_period_days", default=None
    )
