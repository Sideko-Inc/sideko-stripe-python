import pydantic
import typing_extensions


class AccountUnificationAccountControllerFees(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    payer: typing_extensions.Literal[
        "account", "application", "application_custom", "application_express"
    ] = pydantic.Field(
        alias="payer",
    )
    """
    A value indicating the responsible payer of a bundle of Stripe fees for pricing-control eligible products on this account. Learn more about [fee behavior on connected accounts](https://docs.stripe.com/connect/direct-charges-fee-payer-behavior).
    """
