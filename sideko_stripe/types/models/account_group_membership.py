import pydantic
import typing


class AccountGroupMembership(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    payments_pricing: typing.Optional[str] = pydantic.Field(
        alias="payments_pricing", default=None
    )
    """
    The group the account is in to determine their payments pricing, and null if the account is on customized pricing. [See the Platform pricing tool documentation](https://stripe.com/docs/connect/platform-pricing-tools) for details.
    """
