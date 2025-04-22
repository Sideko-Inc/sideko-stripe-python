import pydantic
import typing
import typing_extensions


class BillingPortalConfigurationCreateBodyFeaturesSubscriptionCancelCancellationReason(
    typing_extensions.TypedDict
):
    """
    BillingPortalConfigurationCreateBodyFeaturesSubscriptionCancelCancellationReason
    """

    enabled: typing_extensions.Required[bool]

    options: typing_extensions.Required[
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


class _SerializerBillingPortalConfigurationCreateBodyFeaturesSubscriptionCancelCancellationReason(
    pydantic.BaseModel
):
    """
    Serializer for BillingPortalConfigurationCreateBodyFeaturesSubscriptionCancelCancellationReason handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    enabled: bool = pydantic.Field(
        alias="enabled",
    )
    options: typing.Union[
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
    ] = pydantic.Field(
        alias="options",
    )
