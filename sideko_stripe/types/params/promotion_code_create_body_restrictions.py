import pydantic
import typing
import typing_extensions

from .promotion_code_create_body_restrictions_currency_options import (
    PromotionCodeCreateBodyRestrictionsCurrencyOptions,
    _SerializerPromotionCodeCreateBodyRestrictionsCurrencyOptions,
)


class PromotionCodeCreateBodyRestrictions(typing_extensions.TypedDict):
    """
    Settings that restrict the redemption of the promotion code.
    """

    currency_options: typing_extensions.NotRequired[
        PromotionCodeCreateBodyRestrictionsCurrencyOptions
    ]

    first_time_transaction: typing_extensions.NotRequired[bool]

    minimum_amount: typing_extensions.NotRequired[int]

    minimum_amount_currency: typing_extensions.NotRequired[str]


class _SerializerPromotionCodeCreateBodyRestrictions(pydantic.BaseModel):
    """
    Serializer for PromotionCodeCreateBodyRestrictions handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    currency_options: typing.Optional[
        _SerializerPromotionCodeCreateBodyRestrictionsCurrencyOptions
    ] = pydantic.Field(alias="currency_options", default=None)
    first_time_transaction: typing.Optional[bool] = pydantic.Field(
        alias="first_time_transaction", default=None
    )
    minimum_amount: typing.Optional[int] = pydantic.Field(
        alias="minimum_amount", default=None
    )
    minimum_amount_currency: typing.Optional[str] = pydantic.Field(
        alias="minimum_amount_currency", default=None
    )
