import pydantic
import typing
import typing_extensions


class IssuingCardCreateBodyShippingCustoms(typing_extensions.TypedDict):
    """
    IssuingCardCreateBodyShippingCustoms
    """

    eori_number: typing_extensions.NotRequired[str]


class _SerializerIssuingCardCreateBodyShippingCustoms(pydantic.BaseModel):
    """
    Serializer for IssuingCardCreateBodyShippingCustoms handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    eori_number: typing.Optional[str] = pydantic.Field(
        alias="eori_number", default=None
    )
