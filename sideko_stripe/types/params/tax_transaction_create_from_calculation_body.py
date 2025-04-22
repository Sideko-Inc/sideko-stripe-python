import pydantic
import typing
import typing_extensions

from .tax_transaction_create_from_calculation_body_metadata import (
    TaxTransactionCreateFromCalculationBodyMetadata,
    _SerializerTaxTransactionCreateFromCalculationBodyMetadata,
)


class TaxTransactionCreateFromCalculationBody(typing_extensions.TypedDict, total=False):
    """
    TaxTransactionCreateFromCalculationBody
    """

    calculation: typing_extensions.Required[str]
    """
    Tax Calculation ID to be used as input when creating the transaction.
    """

    expand: typing_extensions.NotRequired[typing.List[str]]
    """
    Specifies which fields in the response should be expanded.
    """

    metadata: typing_extensions.NotRequired[
        TaxTransactionCreateFromCalculationBodyMetadata
    ]
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    """

    posted_at: typing_extensions.NotRequired[int]
    """
    The Unix timestamp representing when the tax liability is assumed or reduced, which determines the liability posting period and handling in tax liability reports. The timestamp must fall within the `tax_date` and the current time, unless the `tax_date` is scheduled in advance. Defaults to the current time.
    """

    reference: typing_extensions.Required[str]
    """
    A custom order or sale identifier, such as 'myOrder_123'. Must be unique across all transactions, including reversals.
    """


class _SerializerTaxTransactionCreateFromCalculationBody(pydantic.BaseModel):
    """
    Serializer for TaxTransactionCreateFromCalculationBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, typing.Any]

    calculation: str = pydantic.Field(
        alias="calculation",
    )
    expand: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="expand", default=None
    )
    metadata: typing.Optional[
        _SerializerTaxTransactionCreateFromCalculationBodyMetadata
    ] = pydantic.Field(alias="metadata", default=None)
    posted_at: typing.Optional[int] = pydantic.Field(alias="posted_at", default=None)
    reference: str = pydantic.Field(
        alias="reference",
    )
