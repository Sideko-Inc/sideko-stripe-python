import pydantic
import typing
import typing_extensions


class IssuingCardCreateBodyPin(typing_extensions.TypedDict):
    """
    The desired PIN for this card.
    """

    encrypted_number: typing_extensions.NotRequired[str]


class _SerializerIssuingCardCreateBodyPin(pydantic.BaseModel):
    """
    Serializer for IssuingCardCreateBodyPin handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    encrypted_number: typing.Optional[str] = pydantic.Field(
        alias="encrypted_number", default=None
    )
