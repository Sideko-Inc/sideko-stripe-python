import pydantic
import typing
import typing_extensions


class DisputePaymentMethodDetailsCard(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    brand: str = pydantic.Field(
        alias="brand",
    )
    """
    Card brand. Can be `amex`, `diners`, `discover`, `eftpos_au`, `jcb`, `link`, `mastercard`, `unionpay`, `visa`, or `unknown`.
    """
    case_type: typing_extensions.Literal["chargeback", "inquiry"] = pydantic.Field(
        alias="case_type",
    )
    """
    The type of dispute opened. Different case types may have varying fees and financial impact.
    """
    network_reason_code: typing.Optional[str] = pydantic.Field(
        alias="network_reason_code", default=None
    )
    """
    The card network's specific dispute reason code, which maps to one of Stripe's primary dispute categories to simplify response guidance. The [Network code map](https://stripe.com/docs/disputes/categories#network-code-map) lists all available dispute reason codes by network.
    """
