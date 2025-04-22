import pydantic
import typing


class ExchangeRateRates(pydantic.BaseModel):
    """
    Hash where the keys are supported currencies and the values are the exchange rate at which the base id currency converts to the key currency.
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
        extra="allow",
    )

    __pydantic_extra__: typing.Dict[str, float]
