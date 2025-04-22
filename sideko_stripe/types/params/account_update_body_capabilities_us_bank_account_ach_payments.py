import pydantic
import typing
import typing_extensions


class AccountUpdateBodyCapabilitiesUsBankAccountAchPayments(
    typing_extensions.TypedDict
):
    """
    AccountUpdateBodyCapabilitiesUsBankAccountAchPayments
    """

    requested: typing_extensions.NotRequired[bool]


class _SerializerAccountUpdateBodyCapabilitiesUsBankAccountAchPayments(
    pydantic.BaseModel
):
    """
    Serializer for AccountUpdateBodyCapabilitiesUsBankAccountAchPayments handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    requested: typing.Optional[bool] = pydantic.Field(alias="requested", default=None)
