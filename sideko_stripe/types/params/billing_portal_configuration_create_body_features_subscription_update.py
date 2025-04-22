import pydantic
import typing
import typing_extensions

from .billing_portal_configuration_create_body_features_subscription_update_products_arr0_item import (
    BillingPortalConfigurationCreateBodyFeaturesSubscriptionUpdateProductsArr0Item,
    _SerializerBillingPortalConfigurationCreateBodyFeaturesSubscriptionUpdateProductsArr0Item,
)
from .billing_portal_configuration_create_body_features_subscription_update_schedule_at_period_end import (
    BillingPortalConfigurationCreateBodyFeaturesSubscriptionUpdateScheduleAtPeriodEnd,
    _SerializerBillingPortalConfigurationCreateBodyFeaturesSubscriptionUpdateScheduleAtPeriodEnd,
)


class BillingPortalConfigurationCreateBodyFeaturesSubscriptionUpdate(
    typing_extensions.TypedDict
):
    """
    BillingPortalConfigurationCreateBodyFeaturesSubscriptionUpdate
    """

    default_allowed_updates: typing_extensions.NotRequired[
        typing.Union[
            typing.List[
                typing_extensions.Literal["price", "promotion_code", "quantity"]
            ],
            str,
        ]
    ]

    enabled: typing_extensions.Required[bool]

    products: typing_extensions.NotRequired[
        typing.Union[
            typing.List[
                BillingPortalConfigurationCreateBodyFeaturesSubscriptionUpdateProductsArr0Item
            ],
            str,
        ]
    ]

    proration_behavior: typing_extensions.NotRequired[
        typing_extensions.Literal["always_invoice", "create_prorations", "none"]
    ]

    schedule_at_period_end: typing_extensions.NotRequired[
        BillingPortalConfigurationCreateBodyFeaturesSubscriptionUpdateScheduleAtPeriodEnd
    ]


class _SerializerBillingPortalConfigurationCreateBodyFeaturesSubscriptionUpdate(
    pydantic.BaseModel
):
    """
    Serializer for BillingPortalConfigurationCreateBodyFeaturesSubscriptionUpdate handling case conversions
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
    enabled: bool = pydantic.Field(
        alias="enabled",
    )
    products: typing.Optional[
        typing.Union[
            typing.List[
                _SerializerBillingPortalConfigurationCreateBodyFeaturesSubscriptionUpdateProductsArr0Item
            ],
            str,
        ]
    ] = pydantic.Field(alias="products", default=None)
    proration_behavior: typing.Optional[
        typing_extensions.Literal["always_invoice", "create_prorations", "none"]
    ] = pydantic.Field(alias="proration_behavior", default=None)
    schedule_at_period_end: typing.Optional[
        _SerializerBillingPortalConfigurationCreateBodyFeaturesSubscriptionUpdateScheduleAtPeriodEnd
    ] = pydantic.Field(alias="schedule_at_period_end", default=None)
