import pydantic
import typing_extensions


class IssuingAuthorizationAuthenticationExemption(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    claimed_by: typing_extensions.Literal["acquirer", "issuer"] = pydantic.Field(
        alias="claimed_by",
    )
    """
    The entity that requested the exemption, either the acquiring merchant or the Issuing user.
    """
    type_: typing_extensions.Literal[
        "low_value_transaction", "transaction_risk_analysis", "unknown"
    ] = pydantic.Field(
        alias="type",
    )
    """
    The specific exemption claimed for this authorization.
    """
