import pydantic
import typing


class ChargeFraudDetails(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    stripe_report: typing.Optional[str] = pydantic.Field(
        alias="stripe_report", default=None
    )
    """
    Assessments from Stripe. If set, the value is `fraudulent`.
    """
    user_report: typing.Optional[str] = pydantic.Field(
        alias="user_report", default=None
    )
    """
    Assessments reported by you. If set, possible values of are `safe` and `fraudulent`.
    """
