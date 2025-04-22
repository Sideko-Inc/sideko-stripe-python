import pydantic
import typing
import typing_extensions


class ShippingRateUpdateBodyFixedAmountCurrencyOptionsAdditionalProps(
    typing_extensions.TypedDict
):
    """
    ShippingRateUpdateBodyFixedAmountCurrencyOptionsAdditionalProps
    """

    amount: typing_extensions.NotRequired[int]

    tax_behavior: typing_extensions.NotRequired[
        typing_extensions.Literal["exclusive", "inclusive", "unspecified"]
    ]


class _SerializerShippingRateUpdateBodyFixedAmountCurrencyOptionsAdditionalProps(
    pydantic.BaseModel
):
    """
    Serializer for ShippingRateUpdateBodyFixedAmountCurrencyOptionsAdditionalProps handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    amount: typing.Optional[int] = pydantic.Field(alias="amount", default=None)
    tax_behavior: typing.Optional[
        typing_extensions.Literal["exclusive", "inclusive", "unspecified"]
    ] = pydantic.Field(alias="tax_behavior", default=None)
