import pydantic
import typing_extensions


class CouponUpdateBodyCurrencyOptionsAdditionalProps(typing_extensions.TypedDict):
    """
    CouponUpdateBodyCurrencyOptionsAdditionalProps
    """

    amount_off: typing_extensions.Required[int]


class _SerializerCouponUpdateBodyCurrencyOptionsAdditionalProps(pydantic.BaseModel):
    """
    Serializer for CouponUpdateBodyCurrencyOptionsAdditionalProps handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    amount_off: int = pydantic.Field(
        alias="amount_off",
    )
