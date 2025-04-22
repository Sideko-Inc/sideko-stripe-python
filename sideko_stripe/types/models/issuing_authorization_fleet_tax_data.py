import pydantic
import typing


class IssuingAuthorizationFleetTaxData(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    local_amount_decimal: typing.Optional[str] = pydantic.Field(
        alias="local_amount_decimal", default=None
    )
    """
    Amount of state or provincial Sales Tax included in the transaction amount. `null` if not reported by merchant or not subject to tax.
    """
    national_amount_decimal: typing.Optional[str] = pydantic.Field(
        alias="national_amount_decimal", default=None
    )
    """
    Amount of national Sales Tax or VAT included in the transaction amount. `null` if not reported by merchant or not subject to tax.
    """
