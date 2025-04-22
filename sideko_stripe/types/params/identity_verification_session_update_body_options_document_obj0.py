import pydantic
import typing
import typing_extensions


class IdentityVerificationSessionUpdateBodyOptionsDocumentObj0(
    typing_extensions.TypedDict
):
    """
    IdentityVerificationSessionUpdateBodyOptionsDocumentObj0
    """

    allowed_types: typing_extensions.NotRequired[
        typing.List[typing_extensions.Literal["driving_license", "id_card", "passport"]]
    ]

    require_id_number: typing_extensions.NotRequired[bool]

    require_live_capture: typing_extensions.NotRequired[bool]

    require_matching_selfie: typing_extensions.NotRequired[bool]


class _SerializerIdentityVerificationSessionUpdateBodyOptionsDocumentObj0(
    pydantic.BaseModel
):
    """
    Serializer for IdentityVerificationSessionUpdateBodyOptionsDocumentObj0 handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    allowed_types: typing.Optional[
        typing.List[typing_extensions.Literal["driving_license", "id_card", "passport"]]
    ] = pydantic.Field(alias="allowed_types", default=None)
    require_id_number: typing.Optional[bool] = pydantic.Field(
        alias="require_id_number", default=None
    )
    require_live_capture: typing.Optional[bool] = pydantic.Field(
        alias="require_live_capture", default=None
    )
    require_matching_selfie: typing.Optional[bool] = pydantic.Field(
        alias="require_matching_selfie", default=None
    )
