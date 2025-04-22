import pydantic
import typing
import typing_extensions


class InvoiceLineUpdateBodyTaxAmountsArr0ItemTaxRateData(typing_extensions.TypedDict):
    """
    InvoiceLineUpdateBodyTaxAmountsArr0ItemTaxRateData
    """

    country: typing_extensions.NotRequired[str]

    description: typing_extensions.NotRequired[str]

    display_name: typing_extensions.Required[str]

    inclusive: typing_extensions.Required[bool]

    jurisdiction: typing_extensions.NotRequired[str]

    jurisdiction_level: typing_extensions.NotRequired[
        typing_extensions.Literal[
            "city", "country", "county", "district", "multiple", "state"
        ]
    ]

    percentage: typing_extensions.Required[float]

    state: typing_extensions.NotRequired[str]

    tax_type: typing_extensions.NotRequired[
        typing_extensions.Literal[
            "amusement_tax",
            "communications_tax",
            "gst",
            "hst",
            "igst",
            "jct",
            "lease_tax",
            "pst",
            "qst",
            "retail_delivery_fee",
            "rst",
            "sales_tax",
            "service_tax",
            "vat",
        ]
    ]


class _SerializerInvoiceLineUpdateBodyTaxAmountsArr0ItemTaxRateData(pydantic.BaseModel):
    """
    Serializer for InvoiceLineUpdateBodyTaxAmountsArr0ItemTaxRateData handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    country: typing.Optional[str] = pydantic.Field(alias="country", default=None)
    description: typing.Optional[str] = pydantic.Field(
        alias="description", default=None
    )
    display_name: str = pydantic.Field(
        alias="display_name",
    )
    inclusive: bool = pydantic.Field(
        alias="inclusive",
    )
    jurisdiction: typing.Optional[str] = pydantic.Field(
        alias="jurisdiction", default=None
    )
    jurisdiction_level: typing.Optional[
        typing_extensions.Literal[
            "city", "country", "county", "district", "multiple", "state"
        ]
    ] = pydantic.Field(alias="jurisdiction_level", default=None)
    percentage: float = pydantic.Field(
        alias="percentage",
    )
    state: typing.Optional[str] = pydantic.Field(alias="state", default=None)
    tax_type: typing.Optional[
        typing_extensions.Literal[
            "amusement_tax",
            "communications_tax",
            "gst",
            "hst",
            "igst",
            "jct",
            "lease_tax",
            "pst",
            "qst",
            "retail_delivery_fee",
            "rst",
            "sales_tax",
            "service_tax",
            "vat",
        ]
    ] = pydantic.Field(alias="tax_type", default=None)
