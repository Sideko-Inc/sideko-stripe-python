import pydantic
import typing
import typing_extensions


class CheckoutSessionCreateBodyPaymentMethodOptionsCardRestrictions(
    typing_extensions.TypedDict
):
    """
    CheckoutSessionCreateBodyPaymentMethodOptionsCardRestrictions
    """

    brands_blocked: typing_extensions.NotRequired[
        typing.List[
            typing_extensions.Literal[
                "american_express", "discover_global_network", "mastercard", "visa"
            ]
        ]
    ]


class _SerializerCheckoutSessionCreateBodyPaymentMethodOptionsCardRestrictions(
    pydantic.BaseModel
):
    """
    Serializer for CheckoutSessionCreateBodyPaymentMethodOptionsCardRestrictions handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    brands_blocked: typing.Optional[
        typing.List[
            typing_extensions.Literal[
                "american_express", "discover_global_network", "mastercard", "visa"
            ]
        ]
    ] = pydantic.Field(alias="brands_blocked", default=None)
