import pydantic
import typing
import typing_extensions


class AccountUpdateBodyCapabilitiesIndiaInternationalPayments(
    typing_extensions.TypedDict
):
    """
    AccountUpdateBodyCapabilitiesIndiaInternationalPayments
    """

    requested: typing_extensions.NotRequired[bool]


class _SerializerAccountUpdateBodyCapabilitiesIndiaInternationalPayments(
    pydantic.BaseModel
):
    """
    Serializer for AccountUpdateBodyCapabilitiesIndiaInternationalPayments handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    requested: typing.Optional[bool] = pydantic.Field(alias="requested", default=None)
