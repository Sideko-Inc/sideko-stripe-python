import pydantic
import typing
import typing_extensions


class PaymentMethodDetailsCardInstallmentsPlan(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    count: typing.Optional[int] = pydantic.Field(alias="count", default=None)
    """
    For `fixed_count` installment plans, this is the number of installment payments your customer will make to their credit card.
    """
    interval: typing.Optional[typing_extensions.Literal["month"]] = pydantic.Field(
        alias="interval", default=None
    )
    """
    For `fixed_count` installment plans, this is the interval between installment payments your customer will make to their credit card.
    One of `month`.
    """
    type_: typing_extensions.Literal["fixed_count"] = pydantic.Field(
        alias="type",
    )
    """
    Type of installment plan, one of `fixed_count`.
    """
