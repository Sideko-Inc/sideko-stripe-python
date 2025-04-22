import pydantic
import typing
import typing_extensions


class CheckoutSessionCreateBodyPaymentMethodOptionsUsBankAccountFinancialConnections(
    typing_extensions.TypedDict
):
    """
    CheckoutSessionCreateBodyPaymentMethodOptionsUsBankAccountFinancialConnections
    """

    permissions: typing_extensions.NotRequired[
        typing.List[
            typing_extensions.Literal[
                "balances", "ownership", "payment_method", "transactions"
            ]
        ]
    ]

    prefetch: typing_extensions.NotRequired[
        typing.List[typing_extensions.Literal["balances", "ownership", "transactions"]]
    ]


class _SerializerCheckoutSessionCreateBodyPaymentMethodOptionsUsBankAccountFinancialConnections(
    pydantic.BaseModel
):
    """
    Serializer for CheckoutSessionCreateBodyPaymentMethodOptionsUsBankAccountFinancialConnections handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    permissions: typing.Optional[
        typing.List[
            typing_extensions.Literal[
                "balances", "ownership", "payment_method", "transactions"
            ]
        ]
    ] = pydantic.Field(alias="permissions", default=None)
    prefetch: typing.Optional[
        typing.List[typing_extensions.Literal["balances", "ownership", "transactions"]]
    ] = pydantic.Field(alias="prefetch", default=None)
