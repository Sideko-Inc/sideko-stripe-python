import pydantic
import typing
import typing_extensions


class AccountCreateBodyCapabilitiesJcbPayments(typing_extensions.TypedDict):
    """
    AccountCreateBodyCapabilitiesJcbPayments
    """

    requested: typing_extensions.NotRequired[bool]


class _SerializerAccountCreateBodyCapabilitiesJcbPayments(pydantic.BaseModel):
    """
    Serializer for AccountCreateBodyCapabilitiesJcbPayments handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    requested: typing.Optional[bool] = pydantic.Field(alias="requested", default=None)
