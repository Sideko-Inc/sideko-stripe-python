import pydantic
import typing


class ConfirmationTokensResourcePaymentMethodOptionsResourceCard(pydantic.BaseModel):
    """
    This hash contains the card payment method options.
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    cvc_token: typing.Optional[str] = pydantic.Field(alias="cvc_token", default=None)
    """
    The `cvc_update` Token collected from the Payment Element.
    """
