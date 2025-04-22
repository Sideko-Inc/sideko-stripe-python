import pydantic
import typing
import typing_extensions


class AccountCreateBodyCapabilitiesTaxReportingUs1099Misc(typing_extensions.TypedDict):
    """
    AccountCreateBodyCapabilitiesTaxReportingUs1099Misc
    """

    requested: typing_extensions.NotRequired[bool]


class _SerializerAccountCreateBodyCapabilitiesTaxReportingUs1099Misc(
    pydantic.BaseModel
):
    """
    Serializer for AccountCreateBodyCapabilitiesTaxReportingUs1099Misc handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    requested: typing.Optional[bool] = pydantic.Field(alias="requested", default=None)
