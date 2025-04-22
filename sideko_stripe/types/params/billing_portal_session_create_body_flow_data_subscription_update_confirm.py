import pydantic
import typing
import typing_extensions

from .billing_portal_session_create_body_flow_data_subscription_update_confirm_discounts_item import (
    BillingPortalSessionCreateBodyFlowDataSubscriptionUpdateConfirmDiscountsItem,
    _SerializerBillingPortalSessionCreateBodyFlowDataSubscriptionUpdateConfirmDiscountsItem,
)
from .billing_portal_session_create_body_flow_data_subscription_update_confirm_items_item import (
    BillingPortalSessionCreateBodyFlowDataSubscriptionUpdateConfirmItemsItem,
    _SerializerBillingPortalSessionCreateBodyFlowDataSubscriptionUpdateConfirmItemsItem,
)


class BillingPortalSessionCreateBodyFlowDataSubscriptionUpdateConfirm(
    typing_extensions.TypedDict
):
    """
    BillingPortalSessionCreateBodyFlowDataSubscriptionUpdateConfirm
    """

    discounts: typing_extensions.NotRequired[
        typing.List[
            BillingPortalSessionCreateBodyFlowDataSubscriptionUpdateConfirmDiscountsItem
        ]
    ]

    items: typing_extensions.Required[
        typing.List[
            BillingPortalSessionCreateBodyFlowDataSubscriptionUpdateConfirmItemsItem
        ]
    ]

    subscription: typing_extensions.Required[str]


class _SerializerBillingPortalSessionCreateBodyFlowDataSubscriptionUpdateConfirm(
    pydantic.BaseModel
):
    """
    Serializer for BillingPortalSessionCreateBodyFlowDataSubscriptionUpdateConfirm handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    discounts: typing.Optional[
        typing.List[
            _SerializerBillingPortalSessionCreateBodyFlowDataSubscriptionUpdateConfirmDiscountsItem
        ]
    ] = pydantic.Field(alias="discounts", default=None)
    items: typing.List[
        _SerializerBillingPortalSessionCreateBodyFlowDataSubscriptionUpdateConfirmItemsItem
    ] = pydantic.Field(
        alias="items",
    )
    subscription: str = pydantic.Field(
        alias="subscription",
    )
