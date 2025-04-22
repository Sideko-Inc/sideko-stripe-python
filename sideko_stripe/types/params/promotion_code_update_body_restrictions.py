import pydantic
import typing
import typing_extensions

from .promotion_code_update_body_restrictions_currency_options import (
    PromotionCodeUpdateBodyRestrictionsCurrencyOptions,
    _SerializerPromotionCodeUpdateBodyRestrictionsCurrencyOptions,
)


class PromotionCodeUpdateBodyRestrictions(typing_extensions.TypedDict):
    """
    Settings that restrict the redemption of the promotion code.
    """

    currency_options: typing_extensions.NotRequired[
        PromotionCodeUpdateBodyRestrictionsCurrencyOptions
    ]


class _SerializerPromotionCodeUpdateBodyRestrictions(pydantic.BaseModel):
    """
    Serializer for PromotionCodeUpdateBodyRestrictions handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    currency_options: typing.Optional[
        _SerializerPromotionCodeUpdateBodyRestrictionsCurrencyOptions
    ] = pydantic.Field(alias="currency_options", default=None)
