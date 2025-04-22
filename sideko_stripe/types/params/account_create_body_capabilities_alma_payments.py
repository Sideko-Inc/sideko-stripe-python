import pydantic
import typing
import typing_extensions


class AccountCreateBodyCapabilitiesAlmaPayments(typing_extensions.TypedDict):
    """
    AccountCreateBodyCapabilitiesAlmaPayments
    """

    requested: typing_extensions.NotRequired[bool]


class _SerializerAccountCreateBodyCapabilitiesAlmaPayments(pydantic.BaseModel):
    """
    Serializer for AccountCreateBodyCapabilitiesAlmaPayments handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    requested: typing.Optional[bool] = pydantic.Field(alias="requested", default=None)
