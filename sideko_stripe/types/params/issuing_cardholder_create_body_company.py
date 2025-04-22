import pydantic
import typing
import typing_extensions


class IssuingCardholderCreateBodyCompany(typing_extensions.TypedDict):
    """
    Additional information about a `company` cardholder.
    """

    tax_id: typing_extensions.NotRequired[str]


class _SerializerIssuingCardholderCreateBodyCompany(pydantic.BaseModel):
    """
    Serializer for IssuingCardholderCreateBodyCompany handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    tax_id: typing.Optional[str] = pydantic.Field(alias="tax_id", default=None)
