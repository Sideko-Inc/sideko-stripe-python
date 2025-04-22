import pydantic
import typing
import typing_extensions

from .billing_clocks_resource_status_details_status_details import (
    BillingClocksResourceStatusDetailsStatusDetails,
)


class TestHelpersTestClock(pydantic.BaseModel):
    """
    A test clock enables deterministic control over objects in testmode. With a test clock, you can create
    objects at a frozen time in the past or future, and advance to a specific future time to observe webhooks and state changes. After the clock advances,
    you can either validate the current state of your scenario (and test your assumptions), change the current state of your scenario (and test more complex scenarios), or keep advancing forward in time.
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    created: int = pydantic.Field(
        alias="created",
    )
    """
    Time at which the object was created. Measured in seconds since the Unix epoch.
    """
    deletes_after: int = pydantic.Field(
        alias="deletes_after",
    )
    """
    Time at which this clock is scheduled to auto delete.
    """
    frozen_time: int = pydantic.Field(
        alias="frozen_time",
    )
    """
    Time at which all objects belonging to this clock are frozen.
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
    name: typing.Optional[str] = pydantic.Field(alias="name", default=None)
    """
    The custom name supplied at creation.
    """
    object: typing_extensions.Literal["test_helpers.test_clock"] = pydantic.Field(
        alias="object",
    )
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    status: typing_extensions.Literal["advancing", "internal_failure", "ready"] = (
        pydantic.Field(
            alias="status",
        )
    )
    """
    The status of the Test Clock.
    """
    status_details: BillingClocksResourceStatusDetailsStatusDetails = pydantic.Field(
        alias="status_details",
    )
