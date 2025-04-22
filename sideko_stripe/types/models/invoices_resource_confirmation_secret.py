import pydantic


class InvoicesResourceConfirmationSecret(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    client_secret: str = pydantic.Field(
        alias="client_secret",
    )
    """
    The client_secret of the payment that Stripe creates for the invoice after finalization.
    """
    type_: str = pydantic.Field(
        alias="type",
    )
    """
    The type of client_secret. Currently this is always payment_intent, referencing the default payment_intent that Stripe creates during invoice finalization
    """
