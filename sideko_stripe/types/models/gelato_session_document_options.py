import pydantic
import typing
import typing_extensions


class GelatoSessionDocumentOptions(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    allowed_types: typing.Optional[
        typing.List[typing_extensions.Literal["driving_license", "id_card", "passport"]]
    ] = pydantic.Field(alias="allowed_types", default=None)
    """
    Array of strings of allowed identity document types. If the provided identity document isn’t one of the allowed types, the verification check will fail with a document_type_not_allowed error code.
    """
    require_id_number: typing.Optional[bool] = pydantic.Field(
        alias="require_id_number", default=None
    )
    """
    Collect an ID number and perform an [ID number check](https://stripe.com/docs/identity/verification-checks?type=id-number) with the document’s extracted name and date of birth.
    """
    require_live_capture: typing.Optional[bool] = pydantic.Field(
        alias="require_live_capture", default=None
    )
    """
    Disable image uploads, identity document images have to be captured using the device’s camera.
    """
    require_matching_selfie: typing.Optional[bool] = pydantic.Field(
        alias="require_matching_selfie", default=None
    )
    """
    Capture a face image and perform a [selfie check](https://stripe.com/docs/identity/verification-checks?type=selfie) comparing a photo ID and a picture of your user’s face. [Learn more](https://stripe.com/docs/identity/selfie).
    """
