import pydantic
import typing


class PaymentMethodCardChecks(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    address_line1_check: typing.Optional[str] = pydantic.Field(
        alias="address_line1_check", default=None
    )
    """
    If a address line1 was provided, results of the check, one of `pass`, `fail`, `unavailable`, or `unchecked`.
    """
    address_postal_code_check: typing.Optional[str] = pydantic.Field(
        alias="address_postal_code_check", default=None
    )
    """
    If a address postal code was provided, results of the check, one of `pass`, `fail`, `unavailable`, or `unchecked`.
    """
    cvc_check: typing.Optional[str] = pydantic.Field(alias="cvc_check", default=None)
    """
    If a CVC was provided, results of the check, one of `pass`, `fail`, `unavailable`, or `unchecked`.
    """
