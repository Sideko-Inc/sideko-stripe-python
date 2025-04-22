import pydantic
import typing
import typing_extensions


class IssuingCardUpdateBodyPin(typing_extensions.TypedDict):
    """
    The desired new PIN for this card.
    """

    encrypted_number: typing_extensions.NotRequired[str]


class _SerializerIssuingCardUpdateBodyPin(pydantic.BaseModel):
    """
    Serializer for IssuingCardUpdateBodyPin handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    encrypted_number: typing.Optional[str] = pydantic.Field(
        alias="encrypted_number", default=None
    )
