import pydantic
import typing
import typing_extensions


class TaxRegistrationCreateBodyCountryOptionsUsStateSalesTaxElectionsItem(
    typing_extensions.TypedDict
):
    """
    TaxRegistrationCreateBodyCountryOptionsUsStateSalesTaxElectionsItem
    """

    jurisdiction: typing_extensions.NotRequired[str]

    type_: typing_extensions.Required[
        typing_extensions.Literal[
            "local_use_tax", "simplified_sellers_use_tax", "single_local_use_tax"
        ]
    ]


class _SerializerTaxRegistrationCreateBodyCountryOptionsUsStateSalesTaxElectionsItem(
    pydantic.BaseModel
):
    """
    Serializer for TaxRegistrationCreateBodyCountryOptionsUsStateSalesTaxElectionsItem handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    jurisdiction: typing.Optional[str] = pydantic.Field(
        alias="jurisdiction", default=None
    )
    type_: typing_extensions.Literal[
        "local_use_tax", "simplified_sellers_use_tax", "single_local_use_tax"
    ] = pydantic.Field(
        alias="type",
    )
