import pydantic
import typing
import typing_extensions


class CheckoutSessionCreateBodyShippingOptionsItemShippingRateDataFixedAmountCurrencyOptionsAdditionalProps(
    typing_extensions.TypedDict
):
    """
    CheckoutSessionCreateBodyShippingOptionsItemShippingRateDataFixedAmountCurrencyOptionsAdditionalProps
    """

    amount: typing_extensions.Required[int]

    tax_behavior: typing_extensions.NotRequired[
        typing_extensions.Literal["exclusive", "inclusive", "unspecified"]
    ]


class _SerializerCheckoutSessionCreateBodyShippingOptionsItemShippingRateDataFixedAmountCurrencyOptionsAdditionalProps(
    pydantic.BaseModel
):
    """
    Serializer for CheckoutSessionCreateBodyShippingOptionsItemShippingRateDataFixedAmountCurrencyOptionsAdditionalProps handling case conversions
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
