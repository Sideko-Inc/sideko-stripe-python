import pydantic


class PaymentMethodDetailsCardNetworkToken(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    used: bool = pydantic.Field(
        alias="used",
    )
    """
    Indicates if Stripe used a network token, either user provided or Stripe managed when processing the transaction.
    """
