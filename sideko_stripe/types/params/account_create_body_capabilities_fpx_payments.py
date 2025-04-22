import pydantic
import typing
import typing_extensions


class AccountCreateBodyCapabilitiesFpxPayments(typing_extensions.TypedDict):
    """
    AccountCreateBodyCapabilitiesFpxPayments
    """

    requested: typing_extensions.NotRequired[bool]


class _SerializerAccountCreateBodyCapabilitiesFpxPayments(pydantic.BaseModel):
    """
    Serializer for AccountCreateBodyCapabilitiesFpxPayments handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    requested: typing.Optional[bool] = pydantic.Field(alias="requested", default=None)
