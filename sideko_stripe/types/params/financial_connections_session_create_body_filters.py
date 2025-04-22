import pydantic
import typing
import typing_extensions


class FinancialConnectionsSessionCreateBodyFilters(typing_extensions.TypedDict):
    """
    Filters to restrict the kinds of accounts to collect.
    """

    account_subcategories: typing_extensions.NotRequired[
        typing.List[
            typing_extensions.Literal[
                "checking", "credit_card", "line_of_credit", "mortgage", "savings"
            ]
        ]
    ]

    countries: typing_extensions.NotRequired[typing.List[str]]


class _SerializerFinancialConnectionsSessionCreateBodyFilters(pydantic.BaseModel):
    """
    Serializer for FinancialConnectionsSessionCreateBodyFilters handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    account_subcategories: typing.Optional[
        typing.List[
            typing_extensions.Literal[
                "checking", "credit_card", "line_of_credit", "mortgage", "savings"
            ]
        ]
    ] = pydantic.Field(alias="account_subcategories", default=None)
    countries: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="countries", default=None
    )
