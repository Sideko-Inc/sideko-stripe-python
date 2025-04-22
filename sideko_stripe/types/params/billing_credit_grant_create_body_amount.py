import pydantic
import typing
import typing_extensions

from .billing_credit_grant_create_body_amount_monetary import (
    BillingCreditGrantCreateBodyAmountMonetary,
    _SerializerBillingCreditGrantCreateBodyAmountMonetary,
)


class BillingCreditGrantCreateBodyAmount(typing_extensions.TypedDict):
    """
    Amount of this credit grant.
    """

    monetary: typing_extensions.NotRequired[BillingCreditGrantCreateBodyAmountMonetary]

    type_: typing_extensions.Required[typing_extensions.Literal["monetary"]]


class _SerializerBillingCreditGrantCreateBodyAmount(pydantic.BaseModel):
    """
    Serializer for BillingCreditGrantCreateBodyAmount handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    monetary: typing.Optional[_SerializerBillingCreditGrantCreateBodyAmountMonetary] = (
        pydantic.Field(alias="monetary", default=None)
    )
    type_: typing_extensions.Literal["monetary"] = pydantic.Field(
        alias="type",
    )
