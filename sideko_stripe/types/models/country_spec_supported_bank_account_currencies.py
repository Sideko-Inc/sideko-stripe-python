import pydantic
import typing


class CountrySpecSupportedBankAccountCurrencies(pydantic.BaseModel):
    """
    Currencies that can be accepted in the specific country (for transfers).
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
        extra="allow",
    )

    __pydantic_extra__: typing.Dict[str, typing.List[str]]
