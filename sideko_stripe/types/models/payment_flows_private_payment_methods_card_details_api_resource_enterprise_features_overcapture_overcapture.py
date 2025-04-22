import pydantic
import typing_extensions


class PaymentFlowsPrivatePaymentMethodsCardDetailsApiResourceEnterpriseFeaturesOvercaptureOvercapture(
    pydantic.BaseModel
):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    maximum_amount_capturable: int = pydantic.Field(
        alias="maximum_amount_capturable",
    )
    """
    The maximum amount that can be captured.
    """
    status: typing_extensions.Literal["available", "unavailable"] = pydantic.Field(
        alias="status",
    )
    """
    Indicates whether or not the authorized amount can be over-captured.
    """
