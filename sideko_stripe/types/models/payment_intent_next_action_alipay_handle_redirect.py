import pydantic
import typing


class PaymentIntentNextActionAlipayHandleRedirect(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    native_data: typing.Optional[str] = pydantic.Field(
        alias="native_data", default=None
    )
    """
    The native data to be used with Alipay SDK you must redirect your customer to in order to authenticate the payment in an Android App.
    """
    native_url: typing.Optional[str] = pydantic.Field(alias="native_url", default=None)
    """
    The native URL you must redirect your customer to in order to authenticate the payment in an iOS App.
    """
    return_url: typing.Optional[str] = pydantic.Field(alias="return_url", default=None)
    """
    If the customer does not exit their browser while authenticating, they will be redirected to this specified URL after completion.
    """
    url: typing.Optional[str] = pydantic.Field(alias="url", default=None)
    """
    The URL you must redirect your customer to in order to authenticate the payment.
    """
