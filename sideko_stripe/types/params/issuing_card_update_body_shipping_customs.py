import pydantic
import typing
import typing_extensions


class IssuingCardUpdateBodyShippingCustoms(typing_extensions.TypedDict):
    """
    IssuingCardUpdateBodyShippingCustoms
    """

    eori_number: typing_extensions.NotRequired[str]


class _SerializerIssuingCardUpdateBodyShippingCustoms(pydantic.BaseModel):
    """
    Serializer for IssuingCardUpdateBodyShippingCustoms handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    eori_number: typing.Optional[str] = pydantic.Field(
        alias="eori_number", default=None
    )
