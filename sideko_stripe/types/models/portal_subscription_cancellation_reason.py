import pydantic
import typing
import typing_extensions


class PortalSubscriptionCancellationReason(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    enabled: bool = pydantic.Field(
        alias="enabled",
    )
    """
    Whether the feature is enabled.
    """
    options: typing.List[
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
    ] = pydantic.Field(
        alias="options",
    )
    """
    Which cancellation reasons will be given as options to the customer.
    """
