import pydantic
import typing
import typing_extensions


class AccountUpdateBodyCapabilitiesAfterpayClearpayPayments(
    typing_extensions.TypedDict
):
    """
    AccountUpdateBodyCapabilitiesAfterpayClearpayPayments
    """

    requested: typing_extensions.NotRequired[bool]


class _SerializerAccountUpdateBodyCapabilitiesAfterpayClearpayPayments(
    pydantic.BaseModel
):
    """
    Serializer for AccountUpdateBodyCapabilitiesAfterpayClearpayPayments handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    requested: typing.Optional[bool] = pydantic.Field(alias="requested", default=None)
