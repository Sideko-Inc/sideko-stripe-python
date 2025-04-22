import pydantic
import typing


class PaymentFlowsPrivatePaymentMethodsAlipayDetails(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    buyer_id: typing.Optional[str] = pydantic.Field(alias="buyer_id", default=None)
    """
    Uniquely identifies this particular Alipay account. You can use this attribute to check whether two Alipay accounts are the same.
    """
    fingerprint: typing.Optional[str] = pydantic.Field(
        alias="fingerprint", default=None
    )
    """
    Uniquely identifies this particular Alipay account. You can use this attribute to check whether two Alipay accounts are the same.
    """
    transaction_id: typing.Optional[str] = pydantic.Field(
        alias="transaction_id", default=None
    )
    """
    Transaction ID of this particular Alipay transaction.
    """
