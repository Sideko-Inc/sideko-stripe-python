import pydantic
import typing_extensions


class ChargeUpdateBodyFraudDetails(typing_extensions.TypedDict):
    """
    A set of key-value pairs you can attach to a charge giving information about its riskiness. If you believe a charge is fraudulent, include a `user_report` key with a value of `fraudulent`. If you believe a charge is safe, include a `user_report` key with a value of `safe`. Stripe will use the information you send to improve our fraud detection algorithms.
    """

    user_report: typing_extensions.Required[
        typing_extensions.Literal["fraudulent", "safe"]
    ]


class _SerializerChargeUpdateBodyFraudDetails(pydantic.BaseModel):
    """
    Serializer for ChargeUpdateBodyFraudDetails handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    user_report: typing_extensions.Literal["fraudulent", "safe"] = pydantic.Field(
        alias="user_report",
    )
