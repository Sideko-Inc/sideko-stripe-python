import pydantic
import typing
import typing_extensions


if typing_extensions.TYPE_CHECKING:
    from .thresholds_resource_usage_threshold_config import (
        ThresholdsResourceUsageThresholdConfig,
    )


class BillingAlert(pydantic.BaseModel):
    """
    A billing alert is a resource that notifies you when a certain usage threshold on a meter is crossed. For example, you might create a billing alert to notify you when a certain user made 100 API requests.
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    alert_type: typing_extensions.Literal["usage_threshold"] = pydantic.Field(
        alias="alert_type",
    )
    """
    Defines the type of the alert.
    """
    id: str = pydantic.Field(
        alias="id",
    )
    """
    Unique identifier for the object.
    """
    livemode: bool = pydantic.Field(
        alias="livemode",
    )
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    object: typing_extensions.Literal["billing.alert"] = pydantic.Field(
        alias="object",
    )
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    status: typing.Optional[
        typing_extensions.Literal["active", "archived", "inactive"]
    ] = pydantic.Field(alias="status", default=None)
    """
    Status of the alert. This can be active, inactive or archived.
    """
    title: str = pydantic.Field(
        alias="title",
    )
    """
    Title of the alert.
    """
    usage_threshold: typing.Optional["ThresholdsResourceUsageThresholdConfig"] = (
        pydantic.Field(alias="usage_threshold", default=None)
    )
    """
    The usage threshold alert configuration enables setting up alerts for when a certain usage threshold on a specific meter is crossed.
    """
