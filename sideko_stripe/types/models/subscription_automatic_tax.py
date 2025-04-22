import pydantic
import typing
import typing_extensions


if typing_extensions.TYPE_CHECKING:
    from .connect_account_reference import ConnectAccountReference


class SubscriptionAutomaticTax(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    disabled_reason: typing.Optional[
        typing_extensions.Literal["requires_location_inputs"]
    ] = pydantic.Field(alias="disabled_reason", default=None)
    """
    If Stripe disabled automatic tax, this enum describes why.
    """
    enabled: bool = pydantic.Field(
        alias="enabled",
    )
    """
    Whether Stripe automatically computes tax on this subscription.
    """
    liability: typing.Optional["ConnectAccountReference"] = pydantic.Field(
        alias="liability", default=None
    )
