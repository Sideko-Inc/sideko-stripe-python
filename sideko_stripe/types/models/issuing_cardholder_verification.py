import pydantic
import typing
import typing_extensions


if typing_extensions.TYPE_CHECKING:
    from .issuing_cardholder_id_document import IssuingCardholderIdDocument


class IssuingCardholderVerification(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    document: typing.Optional["IssuingCardholderIdDocument"] = pydantic.Field(
        alias="document", default=None
    )
