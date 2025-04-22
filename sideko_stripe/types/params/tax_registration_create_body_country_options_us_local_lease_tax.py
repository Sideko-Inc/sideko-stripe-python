import pydantic
import typing_extensions


class TaxRegistrationCreateBodyCountryOptionsUsLocalLeaseTax(
    typing_extensions.TypedDict
):
    """
    TaxRegistrationCreateBodyCountryOptionsUsLocalLeaseTax
    """

    jurisdiction: typing_extensions.Required[str]


class _SerializerTaxRegistrationCreateBodyCountryOptionsUsLocalLeaseTax(
    pydantic.BaseModel
):
    """
    Serializer for TaxRegistrationCreateBodyCountryOptionsUsLocalLeaseTax handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    jurisdiction: str = pydantic.Field(
        alias="jurisdiction",
    )
