import pydantic
import typing
import typing_extensions


class AccountUpdateBodyCapabilitiesJcbPayments(typing_extensions.TypedDict):
    """
    AccountUpdateBodyCapabilitiesJcbPayments
    """

    requested: typing_extensions.NotRequired[bool]


class _SerializerAccountUpdateBodyCapabilitiesJcbPayments(pydantic.BaseModel):
    """
    Serializer for AccountUpdateBodyCapabilitiesJcbPayments handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    requested: typing.Optional[bool] = pydantic.Field(alias="requested", default=None)
