import pydantic
import typing_extensions


class SourceUpdateBodyMandateAcceptanceOffline(typing_extensions.TypedDict):
    """
    SourceUpdateBodyMandateAcceptanceOffline
    """

    contact_email: typing_extensions.Required[str]


class _SerializerSourceUpdateBodyMandateAcceptanceOffline(pydantic.BaseModel):
    """
    Serializer for SourceUpdateBodyMandateAcceptanceOffline handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    contact_email: str = pydantic.Field(
        alias="contact_email",
    )
