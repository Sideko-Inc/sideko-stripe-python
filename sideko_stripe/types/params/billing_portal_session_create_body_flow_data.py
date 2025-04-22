import pydantic
import typing
import typing_extensions

from .billing_portal_session_create_body_flow_data_after_completion import (
    BillingPortalSessionCreateBodyFlowDataAfterCompletion,
    _SerializerBillingPortalSessionCreateBodyFlowDataAfterCompletion,
)
from .billing_portal_session_create_body_flow_data_subscription_cancel import (
    BillingPortalSessionCreateBodyFlowDataSubscriptionCancel,
    _SerializerBillingPortalSessionCreateBodyFlowDataSubscriptionCancel,
)
from .billing_portal_session_create_body_flow_data_subscription_update import (
    BillingPortalSessionCreateBodyFlowDataSubscriptionUpdate,
    _SerializerBillingPortalSessionCreateBodyFlowDataSubscriptionUpdate,
)
from .billing_portal_session_create_body_flow_data_subscription_update_confirm import (
    BillingPortalSessionCreateBodyFlowDataSubscriptionUpdateConfirm,
    _SerializerBillingPortalSessionCreateBodyFlowDataSubscriptionUpdateConfirm,
)


class BillingPortalSessionCreateBodyFlowData(typing_extensions.TypedDict):
    """
    Information about a specific flow for the customer to go through. See the [docs](https://stripe.com/docs/customer-management/portal-deep-links) to learn more about using customer portal deep links and flows.
    """

    after_completion: typing_extensions.NotRequired[
        BillingPortalSessionCreateBodyFlowDataAfterCompletion
    ]

    subscription_cancel: typing_extensions.NotRequired[
        BillingPortalSessionCreateBodyFlowDataSubscriptionCancel
    ]

    subscription_update: typing_extensions.NotRequired[
        BillingPortalSessionCreateBodyFlowDataSubscriptionUpdate
    ]

    subscription_update_confirm: typing_extensions.NotRequired[
        BillingPortalSessionCreateBodyFlowDataSubscriptionUpdateConfirm
    ]

    type_: typing_extensions.Required[
        typing_extensions.Literal[
            "payment_method_update",
            "subscription_cancel",
            "subscription_update",
            "subscription_update_confirm",
        ]
    ]


class _SerializerBillingPortalSessionCreateBodyFlowData(pydantic.BaseModel):
    """
    Serializer for BillingPortalSessionCreateBodyFlowData handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    after_completion: typing.Optional[
        _SerializerBillingPortalSessionCreateBodyFlowDataAfterCompletion
    ] = pydantic.Field(alias="after_completion", default=None)
    subscription_cancel: typing.Optional[
        _SerializerBillingPortalSessionCreateBodyFlowDataSubscriptionCancel
    ] = pydantic.Field(alias="subscription_cancel", default=None)
    subscription_update: typing.Optional[
        _SerializerBillingPortalSessionCreateBodyFlowDataSubscriptionUpdate
    ] = pydantic.Field(alias="subscription_update", default=None)
    subscription_update_confirm: typing.Optional[
        _SerializerBillingPortalSessionCreateBodyFlowDataSubscriptionUpdateConfirm
    ] = pydantic.Field(alias="subscription_update_confirm", default=None)
    type_: typing_extensions.Literal[
        "payment_method_update",
        "subscription_cancel",
        "subscription_update",
        "subscription_update_confirm",
    ] = pydantic.Field(
        alias="type",
    )
