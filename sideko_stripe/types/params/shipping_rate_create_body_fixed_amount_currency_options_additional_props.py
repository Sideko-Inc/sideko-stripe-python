import pydantic
import typing
import typing_extensions


class ShippingRateCreateBodyFixedAmountCurrencyOptionsAdditionalProps(
    typing_extensions.TypedDict
):
    """
    ShippingRateCreateBodyFixedAmountCurrencyOptionsAdditionalProps
    """

    amount: typing_extensions.Required[int]

    tax_behavior: typing_extensions.NotRequired[
        typing_extensions.Literal["exclusive", "inclusive", "unspecified"]
    ]


class _SerializerShippingRateCreateBodyFixedAmountCurrencyOptionsAdditionalProps(
    pydantic.BaseModel
):
    """
    Serializer for ShippingRateCreateBodyFixedAmountCurrencyOptionsAdditionalProps handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    amount: int = pydantic.Field(
        alias="amount",
    )
    tax_behavior: typing.Optional[
        typing_extensions.Literal["exclusive", "inclusive", "unspecified"]
    ] = pydantic.Field(alias="tax_behavior", default=None)
