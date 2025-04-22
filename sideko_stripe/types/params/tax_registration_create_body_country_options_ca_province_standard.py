import pydantic
import typing_extensions


class TaxRegistrationCreateBodyCountryOptionsCaProvinceStandard(
    typing_extensions.TypedDict
):
    """
    TaxRegistrationCreateBodyCountryOptionsCaProvinceStandard
    """

    province: typing_extensions.Required[str]


class _SerializerTaxRegistrationCreateBodyCountryOptionsCaProvinceStandard(
    pydantic.BaseModel
):
    """
    Serializer for TaxRegistrationCreateBodyCountryOptionsCaProvinceStandard handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    province: str = pydantic.Field(
        alias="province",
    )
