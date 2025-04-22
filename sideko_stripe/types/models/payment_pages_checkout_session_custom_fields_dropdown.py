import pydantic
import typing

from .payment_pages_checkout_session_custom_fields_option import (
    PaymentPagesCheckoutSessionCustomFieldsOption,
)


class PaymentPagesCheckoutSessionCustomFieldsDropdown(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    default_value: typing.Optional[str] = pydantic.Field(
        alias="default_value", default=None
    )
    """
    The value that will pre-fill on the payment page.
    """
    options: typing.List[PaymentPagesCheckoutSessionCustomFieldsOption] = (
        pydantic.Field(
            alias="options",
        )
    )
    """
    The options available for the customer to select. Up to 200 options allowed.
    """
    value: typing.Optional[str] = pydantic.Field(alias="value", default=None)
    """
    The option selected by the customer. This will be the `value` for the option.
    """
