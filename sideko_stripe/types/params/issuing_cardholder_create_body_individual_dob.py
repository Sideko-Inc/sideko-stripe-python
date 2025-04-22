import pydantic
import typing_extensions


class IssuingCardholderCreateBodyIndividualDob(typing_extensions.TypedDict):
    """
    IssuingCardholderCreateBodyIndividualDob
    """

    day: typing_extensions.Required[int]

    month: typing_extensions.Required[int]

    year: typing_extensions.Required[int]


class _SerializerIssuingCardholderCreateBodyIndividualDob(pydantic.BaseModel):
    """
    Serializer for IssuingCardholderCreateBodyIndividualDob handling case conversions
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
