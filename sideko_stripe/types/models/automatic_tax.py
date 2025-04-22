import pydantic
import typing
import typing_extensions


if typing_extensions.TYPE_CHECKING:
    from .connect_account_reference import ConnectAccountReference


class AutomaticTax(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    disabled_reason: typing.Optional[
        typing_extensions.Literal[
            "finalization_requires_location_inputs", "finalization_system_error"
        ]
    ] = pydantic.Field(alias="disabled_reason", default=None)
    """
    If Stripe disabled automatic tax, this enum describes why.
    """
    enabled: bool = pydantic.Field(
        alias="enabled",
    )
    """
    Whether Stripe automatically computes tax on this invoice. Note that incompatible invoice items (invoice items with manually specified [tax rates](https://stripe.com/docs/api/tax_rates), negative amounts, or `tax_behavior=unspecified`) cannot be added to automatic tax invoices.
    """
    liability: typing.Optional["ConnectAccountReference"] = pydantic.Field(
        alias="liability", default=None
    )
    status: typing.Optional[
        typing_extensions.Literal["complete", "failed", "requires_location_inputs"]
    ] = pydantic.Field(alias="status", default=None)
    """
    The status of the most recent automated tax calculation for this invoice.
    """
