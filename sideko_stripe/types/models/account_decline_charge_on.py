import pydantic


class AccountDeclineChargeOn(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    avs_failure: bool = pydantic.Field(
        alias="avs_failure",
    )
    """
    Whether Stripe automatically declines charges with an incorrect ZIP or postal code. This setting only applies when a ZIP or postal code is provided and they fail bank verification.
    """
    cvc_failure: bool = pydantic.Field(
        alias="cvc_failure",
    )
    """
    Whether Stripe automatically declines charges with an incorrect CVC. This setting only applies when a CVC is provided and it fails bank verification.
    """
