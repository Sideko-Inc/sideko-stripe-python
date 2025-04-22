import pydantic
import typing
import typing_extensions


class PaymentIntentUpdateBodyPaymentMethodOptionsUsBankAccountObj0FinancialConnectionsFilters(
    typing_extensions.TypedDict
):
    """
    PaymentIntentUpdateBodyPaymentMethodOptionsUsBankAccountObj0FinancialConnectionsFilters
    """

    account_subcategories: typing_extensions.NotRequired[
        typing.List[typing_extensions.Literal["checking", "savings"]]
    ]


class _SerializerPaymentIntentUpdateBodyPaymentMethodOptionsUsBankAccountObj0FinancialConnectionsFilters(
    pydantic.BaseModel
):
    """
    Serializer for PaymentIntentUpdateBodyPaymentMethodOptionsUsBankAccountObj0FinancialConnectionsFilters handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    account_subcategories: typing.Optional[
        typing.List[typing_extensions.Literal["checking", "savings"]]
    ] = pydantic.Field(alias="account_subcategories", default=None)
