import pydantic
import typing
import typing_extensions


class PaypalSellerProtection(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    dispute_categories: typing.Optional[
        typing.List[typing_extensions.Literal["fraudulent", "product_not_received"]]
    ] = pydantic.Field(alias="dispute_categories", default=None)
    """
    An array of conditions that are covered for the transaction, if applicable.
    """
    status: typing_extensions.Literal[
        "eligible", "not_eligible", "partially_eligible"
    ] = pydantic.Field(
        alias="status",
    )
    """
    Indicates whether the transaction is eligible for PayPal's seller protection.
    """
