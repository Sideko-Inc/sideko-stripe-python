import pydantic
import typing
import typing_extensions


class DisputePaymentMethodDetailsAmazonPay(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    dispute_type: typing.Optional[typing_extensions.Literal["chargeback", "claim"]] = (
        pydantic.Field(alias="dispute_type", default=None)
    )
    """
    The AmazonPay dispute type, chargeback or claim
    """
