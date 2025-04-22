import pydantic
import typing
import typing_extensions

from .billing_portal_configuration_update_body_features_subscription_update_products_arr0_item import (
    BillingPortalConfigurationUpdateBodyFeaturesSubscriptionUpdateProductsArr0Item,
    _SerializerBillingPortalConfigurationUpdateBodyFeaturesSubscriptionUpdateProductsArr0Item,
)
from .billing_portal_configuration_update_body_features_subscription_update_schedule_at_period_end import (
    BillingPortalConfigurationUpdateBodyFeaturesSubscriptionUpdateScheduleAtPeriodEnd,
    _SerializerBillingPortalConfigurationUpdateBodyFeaturesSubscriptionUpdateScheduleAtPeriodEnd,
)


class BillingPortalConfigurationUpdateBodyFeaturesSubscriptionUpdate(
    typing_extensions.TypedDict
):
    """
    BillingPortalConfigurationUpdateBodyFeaturesSubscriptionUpdate
    """

    default_allowed_updates: typing_extensions.NotRequired[
        typing.Union[
            typing.List[
                typing_extensions.Literal["price", "promotion_code", "quantity"]
            ],
            str,
        ]
    ]

    enabled: typing_extensions.NotRequired[bool]

    products: typing_extensions.NotRequired[
        typing.Union[
            typing.List[
                BillingPortalConfigurationUpdateBodyFeaturesSubscriptionUpdateProductsArr0Item
            ],
            str,
        ]
    ]

    proration_behavior: typing_extensions.NotRequired[
        typing_extensions.Literal["always_invoice", "create_prorations", "none"]
    ]

    schedule_at_period_end: typing_extensions.NotRequired[
        BillingPortalConfigurationUpdateBodyFeaturesSubscriptionUpdateScheduleAtPeriodEnd
    ]


class _SerializerBillingPortalConfigurationUpdateBodyFeaturesSubscriptionUpdate(
    pydantic.BaseModel
):
    """
    Serializer for BillingPortalConfigurationUpdateBodyFeaturesSubscriptionUpdate handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    default_allowed_updates: typing.Optional[
        typing.Union[
            typing.List[
                typing_extensions.Literal["price", "promotion_code", "quantity"]
            ],
            str,
        ]
    ] = pydantic.Field(alias="default_allowed_updates", default=None)
    enabled: typing.Optional[bool] = pydantic.Field(alias="enabled", default=None)
    products: typing.Optional[
        typing.Union[
            typing.List[
                _SerializerBillingPortalConfigurationUpdateBodyFeaturesSubscriptionUpdateProductsArr0Item
            ],
            str,
        ]
    ] = pydantic.Field(alias="products", default=None)
    proration_behavior: typing.Optional[
        typing_extensions.Literal["always_invoice", "create_prorations", "none"]
    ] = pydantic.Field(alias="proration_behavior", default=None)
    schedule_at_period_end: typing.Optional[
        _SerializerBillingPortalConfigurationUpdateBodyFeaturesSubscriptionUpdateScheduleAtPeriodEnd
    ] = pydantic.Field(alias="schedule_at_period_end", default=None)
