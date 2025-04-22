import pydantic
import typing


class CheckoutSwishPaymentMethodOptions(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    reference: typing.Optional[str] = pydantic.Field(alias="reference", default=None)
    """
    The order reference that will be displayed to customers in the Swish application. Defaults to the `id` of the Payment Intent.
    """
