import pydantic
import typing
import typing_extensions


if typing_extensions.TYPE_CHECKING:
    from .file import File


class IssuingCardholderIdDocument(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    back: typing.Optional[typing.Union[str, "File"]] = pydantic.Field(
        alias="back", default=None
    )
    """
    The back of a document returned by a [file upload](https://stripe.com/docs/api#create_file) with a `purpose` value of `identity_document`.
    """
    front: typing.Optional[typing.Union[str, "File"]] = pydantic.Field(
        alias="front", default=None
    )
    """
    The front of a document returned by a [file upload](https://stripe.com/docs/api#create_file) with a `purpose` value of `identity_document`.
    """
