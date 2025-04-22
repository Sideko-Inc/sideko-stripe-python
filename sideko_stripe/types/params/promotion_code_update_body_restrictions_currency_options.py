import pydantic
import typing
import typing_extensions

from .promotion_code_update_body_restrictions_currency_options_additional_props import (
    PromotionCodeUpdateBodyRestrictionsCurrencyOptionsAdditionalProps,
    _SerializerPromotionCodeUpdateBodyRestrictionsCurrencyOptionsAdditionalProps,
)


class PromotionCodeUpdateBodyRestrictionsCurrencyOptions(
    typing_extensions.TypedDict, total=False
):
    """
    PromotionCodeUpdateBodyRestrictionsCurrencyOptions
    """


class _SerializerPromotionCodeUpdateBodyRestrictionsCurrencyOptions(pydantic.BaseModel):
    """
    Serializer for PromotionCodeUpdateBodyRestrictionsCurrencyOptions handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[
        str,
        _SerializerPromotionCodeUpdateBodyRestrictionsCurrencyOptionsAdditionalProps,
    ]
