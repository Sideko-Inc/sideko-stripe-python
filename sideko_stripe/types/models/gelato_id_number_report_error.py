import pydantic
import typing
import typing_extensions


class GelatoIdNumberReportError(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    code: typing.Optional[
        typing_extensions.Literal[
            "id_number_insufficient_document_data",
            "id_number_mismatch",
            "id_number_unverified_other",
        ]
    ] = pydantic.Field(alias="code", default=None)
    """
    A short machine-readable string giving the reason for the verification failure.
    """
    reason: typing.Optional[str] = pydantic.Field(alias="reason", default=None)
    """
    A human-readable message giving the reason for the failure. These messages can be shown to your users.
    """
