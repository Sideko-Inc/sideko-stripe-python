import pydantic
import typing
import typing_extensions


class AccountCreateBodyCapabilitiesUsBankAccountAchPayments(
    typing_extensions.TypedDict
):
    """
    AccountCreateBodyCapabilitiesUsBankAccountAchPayments
    """

    requested: typing_extensions.NotRequired[bool]


class _SerializerAccountCreateBodyCapabilitiesUsBankAccountAchPayments(
    pydantic.BaseModel
):
    """
    Serializer for AccountCreateBodyCapabilitiesUsBankAccountAchPayments handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    requested: typing.Optional[bool] = pydantic.Field(alias="requested", default=None)
