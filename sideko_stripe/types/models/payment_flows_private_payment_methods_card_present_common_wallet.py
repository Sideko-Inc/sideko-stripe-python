import pydantic
import typing_extensions


class PaymentFlowsPrivatePaymentMethodsCardPresentCommonWallet(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    type_: typing_extensions.Literal[
        "apple_pay", "google_pay", "samsung_pay", "unknown"
    ] = pydantic.Field(
        alias="type",
    )
    """
    The type of mobile wallet, one of `apple_pay`, `google_pay`, `samsung_pay`, or `unknown`.
    """
