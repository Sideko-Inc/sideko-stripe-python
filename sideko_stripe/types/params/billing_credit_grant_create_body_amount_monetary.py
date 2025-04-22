import pydantic
import typing_extensions


class BillingCreditGrantCreateBodyAmountMonetary(typing_extensions.TypedDict):
    """
    BillingCreditGrantCreateBodyAmountMonetary
    """

    currency: typing_extensions.Required[str]

    value: typing_extensions.Required[int]


class _SerializerBillingCreditGrantCreateBodyAmountMonetary(pydantic.BaseModel):
    """
    Serializer for BillingCreditGrantCreateBodyAmountMonetary handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    currency: str = pydantic.Field(
        alias="currency",
    )
    value: int = pydantic.Field(
        alias="value",
    )
