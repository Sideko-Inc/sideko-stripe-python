import pydantic
import typing
import typing_extensions

from .promotion_code_create_body_restrictions_currency_options_additional_props import (
    PromotionCodeCreateBodyRestrictionsCurrencyOptionsAdditionalProps,
    _SerializerPromotionCodeCreateBodyRestrictionsCurrencyOptionsAdditionalProps,
)


class PromotionCodeCreateBodyRestrictionsCurrencyOptions(
    typing_extensions.TypedDict, total=False
):
    """
    PromotionCodeCreateBodyRestrictionsCurrencyOptions
    """


class _SerializerPromotionCodeCreateBodyRestrictionsCurrencyOptions(pydantic.BaseModel):
    """
    Serializer for PromotionCodeCreateBodyRestrictionsCurrencyOptions handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[
        str,
        _SerializerPromotionCodeCreateBodyRestrictionsCurrencyOptionsAdditionalProps,
    ]
