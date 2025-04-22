import pydantic
import typing
import typing_extensions


class AccountCreateBodyCapabilitiesCardIssuing(typing_extensions.TypedDict):
    """
    AccountCreateBodyCapabilitiesCardIssuing
    """

    requested: typing_extensions.NotRequired[bool]


class _SerializerAccountCreateBodyCapabilitiesCardIssuing(pydantic.BaseModel):
    """
    Serializer for AccountCreateBodyCapabilitiesCardIssuing handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    requested: typing.Optional[bool] = pydantic.Field(alias="requested", default=None)
