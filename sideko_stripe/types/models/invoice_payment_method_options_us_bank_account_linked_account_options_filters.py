import pydantic
import typing
import typing_extensions


class InvoicePaymentMethodOptionsUsBankAccountLinkedAccountOptionsFilters(
    pydantic.BaseModel
):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    account_subcategories: typing.Optional[
        typing.List[typing_extensions.Literal["checking", "savings"]]
    ] = pydantic.Field(alias="account_subcategories", default=None)
    """
    The account subcategories to use to filter for possible accounts to link. Valid subcategories are `checking` and `savings`.
    """
