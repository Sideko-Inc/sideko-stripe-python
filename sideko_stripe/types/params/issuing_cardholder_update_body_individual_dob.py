import pydantic
import typing_extensions


class IssuingCardholderUpdateBodyIndividualDob(typing_extensions.TypedDict):
    """
    IssuingCardholderUpdateBodyIndividualDob
    """

    day: typing_extensions.Required[int]

    month: typing_extensions.Required[int]

    year: typing_extensions.Required[int]


class _SerializerIssuingCardholderUpdateBodyIndividualDob(pydantic.BaseModel):
    """
    Serializer for IssuingCardholderUpdateBodyIndividualDob handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    day: int = pydantic.Field(
        alias="day",
    )
    month: int = pydantic.Field(
        alias="month",
    )
    year: int = pydantic.Field(
        alias="year",
    )
