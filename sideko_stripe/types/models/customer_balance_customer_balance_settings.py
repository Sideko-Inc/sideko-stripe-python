import pydantic
import typing_extensions


class CustomerBalanceCustomerBalanceSettings(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    reconciliation_mode: typing_extensions.Literal["automatic", "manual"] = (
        pydantic.Field(
            alias="reconciliation_mode",
        )
    )
    """
    The configuration for how funds that land in the customer cash balance are reconciled.
    """
    using_merchant_default: bool = pydantic.Field(
        alias="using_merchant_default",
    )
    """
    A flag to indicate if reconciliation mode returned is the user's default or is specific to this customer cash balance
    """
