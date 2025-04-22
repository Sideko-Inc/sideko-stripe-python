import pydantic
import typing
import typing_extensions


class PromotionCodeUpdateBodyRestrictionsCurrencyOptionsAdditionalProps(
    typing_extensions.TypedDict
):
    """
    PromotionCodeUpdateBodyRestrictionsCurrencyOptionsAdditionalProps
    """

    minimum_amount: typing_extensions.NotRequired[int]


class _SerializerPromotionCodeUpdateBodyRestrictionsCurrencyOptionsAdditionalProps(
    pydantic.BaseModel
):
    """
    Serializer for PromotionCodeUpdateBodyRestrictionsCurrencyOptionsAdditionalProps handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    minimum_amount: typing.Optional[int] = pydantic.Field(
        alias="minimum_amount", default=None
    )
