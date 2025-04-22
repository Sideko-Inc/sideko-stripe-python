import pydantic
import typing_extensions


class CouponCreateBodyCurrencyOptionsAdditionalProps(typing_extensions.TypedDict):
    """
    CouponCreateBodyCurrencyOptionsAdditionalProps
    """

    amount_off: typing_extensions.Required[int]


class _SerializerCouponCreateBodyCurrencyOptionsAdditionalProps(pydantic.BaseModel):
    """
    Serializer for CouponCreateBodyCurrencyOptionsAdditionalProps handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    amount_off: int = pydantic.Field(
        alias="amount_off",
    )
