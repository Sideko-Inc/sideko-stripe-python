import pydantic
import typing
import typing_extensions


class AccountUpdateBodySettingsInvoices(typing_extensions.TypedDict):
    """
    AccountUpdateBodySettingsInvoices
    """

    default_account_tax_ids: typing_extensions.NotRequired[
        typing.Union[typing.List[str], str]
    ]

    hosted_payment_method_save: typing_extensions.NotRequired[
        typing_extensions.Literal["always", "never", "offer"]
    ]


class _SerializerAccountUpdateBodySettingsInvoices(pydantic.BaseModel):
    """
    Serializer for AccountUpdateBodySettingsInvoices handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    default_account_tax_ids: typing.Optional[typing.Union[typing.List[str], str]] = (
        pydantic.Field(alias="default_account_tax_ids", default=None)
    )
    hosted_payment_method_save: typing.Optional[
        typing_extensions.Literal["always", "never", "offer"]
    ] = pydantic.Field(alias="hosted_payment_method_save", default=None)
