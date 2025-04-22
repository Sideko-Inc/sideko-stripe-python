import pydantic
import typing
import typing_extensions


class AccountUpdateBodySettingsCardPaymentsDeclineOn(typing_extensions.TypedDict):
    """
    AccountUpdateBodySettingsCardPaymentsDeclineOn
    """

    avs_failure: typing_extensions.NotRequired[bool]

    cvc_failure: typing_extensions.NotRequired[bool]


class _SerializerAccountUpdateBodySettingsCardPaymentsDeclineOn(pydantic.BaseModel):
    """
    Serializer for AccountUpdateBodySettingsCardPaymentsDeclineOn handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    avs_failure: typing.Optional[bool] = pydantic.Field(
        alias="avs_failure", default=None
    )
    cvc_failure: typing.Optional[bool] = pydantic.Field(
        alias="cvc_failure", default=None
    )
