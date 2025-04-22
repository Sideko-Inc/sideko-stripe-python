import pydantic
import typing
import typing_extensions


class BillingPortalConfigurationUpdateBodyFeaturesSubscriptionCancelCancellationReason(
    typing_extensions.TypedDict
):
    """
    BillingPortalConfigurationUpdateBodyFeaturesSubscriptionCancelCancellationReason
    """

    enabled: typing_extensions.Required[bool]

    options: typing_extensions.NotRequired[
        typing.Union[
            typing.List[
                typing_extensions.Literal[
                    "customer_service",
                    "low_quality",
                    "missing_features",
                    "other",
                    "switched_service",
                    "too_complex",
                    "too_expensive",
                    "unused",
                ]
            ],
            str,
        ]
    ]


class _SerializerBillingPortalConfigurationUpdateBodyFeaturesSubscriptionCancelCancellationReason(
    pydantic.BaseModel
):
    """
    Serializer for BillingPortalConfigurationUpdateBodyFeaturesSubscriptionCancelCancellationReason handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    enabled: bool = pydantic.Field(
        alias="enabled",
    )
    options: typing.Optional[
        typing.Union[
            typing.List[
                typing_extensions.Literal[
                    "customer_service",
                    "low_quality",
                    "missing_features",
                    "other",
                    "switched_service",
                    "too_complex",
                    "too_expensive",
                    "unused",
                ]
            ],
            str,
        ]
    ] = pydantic.Field(alias="options", default=None)
