import pydantic
import typing_extensions


class SourceCreateBodyMandateAcceptanceOffline(typing_extensions.TypedDict):
    """
    SourceCreateBodyMandateAcceptanceOffline
    """

    contact_email: typing_extensions.Required[str]


class _SerializerSourceCreateBodyMandateAcceptanceOffline(pydantic.BaseModel):
    """
    Serializer for SourceCreateBodyMandateAcceptanceOffline handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    contact_email: str = pydantic.Field(
        alias="contact_email",
    )
