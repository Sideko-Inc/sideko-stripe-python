import pydantic
import typing
import typing_extensions


class AccountCreateBodyCapabilitiesTaxReportingUs1099K(typing_extensions.TypedDict):
    """
    AccountCreateBodyCapabilitiesTaxReportingUs1099K
    """

    requested: typing_extensions.NotRequired[bool]


class _SerializerAccountCreateBodyCapabilitiesTaxReportingUs1099K(pydantic.BaseModel):
    """
    Serializer for AccountCreateBodyCapabilitiesTaxReportingUs1099K handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    requested: typing.Optional[bool] = pydantic.Field(alias="requested", default=None)
