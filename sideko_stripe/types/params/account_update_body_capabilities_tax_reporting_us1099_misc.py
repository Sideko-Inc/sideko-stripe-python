import pydantic
import typing
import typing_extensions


class AccountUpdateBodyCapabilitiesTaxReportingUs1099Misc(typing_extensions.TypedDict):
    """
    AccountUpdateBodyCapabilitiesTaxReportingUs1099Misc
    """

    requested: typing_extensions.NotRequired[bool]


class _SerializerAccountUpdateBodyCapabilitiesTaxReportingUs1099Misc(
    pydantic.BaseModel
):
    """
    Serializer for AccountUpdateBodyCapabilitiesTaxReportingUs1099Misc handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    requested: typing.Optional[bool] = pydantic.Field(alias="requested", default=None)
