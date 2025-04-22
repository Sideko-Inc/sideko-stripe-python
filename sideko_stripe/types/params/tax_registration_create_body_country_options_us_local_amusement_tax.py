import pydantic
import typing_extensions


class TaxRegistrationCreateBodyCountryOptionsUsLocalAmusementTax(
    typing_extensions.TypedDict
):
    """
    TaxRegistrationCreateBodyCountryOptionsUsLocalAmusementTax
    """

    jurisdiction: typing_extensions.Required[str]


class _SerializerTaxRegistrationCreateBodyCountryOptionsUsLocalAmusementTax(
    pydantic.BaseModel
):
    """
    Serializer for TaxRegistrationCreateBodyCountryOptionsUsLocalAmusementTax handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    jurisdiction: str = pydantic.Field(
        alias="jurisdiction",
    )
