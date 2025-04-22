import pydantic
import typing
import typing_extensions


class AccountUpdateBodyCapabilitiesCardIssuing(typing_extensions.TypedDict):
    """
    AccountUpdateBodyCapabilitiesCardIssuing
    """

    requested: typing_extensions.NotRequired[bool]


class _SerializerAccountUpdateBodyCapabilitiesCardIssuing(pydantic.BaseModel):
    """
    Serializer for AccountUpdateBodyCapabilitiesCardIssuing handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    requested: typing.Optional[bool] = pydantic.Field(alias="requested", default=None)
