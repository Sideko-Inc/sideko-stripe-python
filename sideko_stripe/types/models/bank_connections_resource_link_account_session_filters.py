import pydantic
import typing
import typing_extensions


class BankConnectionsResourceLinkAccountSessionFilters(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    account_subcategories: typing.Optional[
        typing.List[
            typing_extensions.Literal[
                "checking", "credit_card", "line_of_credit", "mortgage", "savings"
            ]
        ]
    ] = pydantic.Field(alias="account_subcategories", default=None)
    """
    Restricts the Session to subcategories of accounts that can be linked. Valid subcategories are: `checking`, `savings`, `mortgage`, `line_of_credit`, `credit_card`.
    """
    countries: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="countries", default=None
    )
    """
    List of countries from which to filter accounts.
    """
