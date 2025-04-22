import pydantic
import typing
import typing_extensions


class SetupIntentUpdateBodyPaymentMethodOptionsUsBankAccountFinancialConnectionsFilters(
    typing_extensions.TypedDict
):
    """
    SetupIntentUpdateBodyPaymentMethodOptionsUsBankAccountFinancialConnectionsFilters
    """

    account_subcategories: typing_extensions.NotRequired[
        typing.List[typing_extensions.Literal["checking", "savings"]]
    ]


class _SerializerSetupIntentUpdateBodyPaymentMethodOptionsUsBankAccountFinancialConnectionsFilters(
    pydantic.BaseModel
):
    """
    Serializer for SetupIntentUpdateBodyPaymentMethodOptionsUsBankAccountFinancialConnectionsFilters handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    account_subcategories: typing.Optional[
        typing.List[typing_extensions.Literal["checking", "savings"]]
    ] = pydantic.Field(alias="account_subcategories", default=None)
