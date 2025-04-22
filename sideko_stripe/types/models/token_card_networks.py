import pydantic
import typing


class TokenCardNetworks(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    preferred: typing.Optional[str] = pydantic.Field(alias="preferred", default=None)
    """
    The preferred network for co-branded cards. Can be `cartes_bancaires`, `mastercard`, `visa` or `invalid_preference` if requested network is not valid for the card.
    """
