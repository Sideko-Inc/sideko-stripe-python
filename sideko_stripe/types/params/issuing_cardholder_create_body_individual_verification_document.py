import pydantic
import typing
import typing_extensions


class IssuingCardholderCreateBodyIndividualVerificationDocument(
    typing_extensions.TypedDict
):
    """
    IssuingCardholderCreateBodyIndividualVerificationDocument
    """

    back: typing_extensions.NotRequired[str]

    front: typing_extensions.NotRequired[str]


class _SerializerIssuingCardholderCreateBodyIndividualVerificationDocument(
    pydantic.BaseModel
):
    """
    Serializer for IssuingCardholderCreateBodyIndividualVerificationDocument handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    back: typing.Optional[str] = pydantic.Field(alias="back", default=None)
    front: typing.Optional[str] = pydantic.Field(alias="front", default=None)
