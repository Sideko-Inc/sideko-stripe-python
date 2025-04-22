import pydantic
import typing


class IssuingNetworkTokenVisa(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    card_reference_id: str = pydantic.Field(
        alias="card_reference_id",
    )
    """
    A unique reference ID from Visa to represent the card account number.
    """
    token_reference_id: str = pydantic.Field(
        alias="token_reference_id",
    )
    """
    The network-unique identifier for the token.
    """
    token_requestor_id: str = pydantic.Field(
        alias="token_requestor_id",
    )
    """
    The ID of the entity requesting tokenization, specific to Visa.
    """
    token_risk_score: typing.Optional[str] = pydantic.Field(
        alias="token_risk_score", default=None
    )
    """
    Degree of risk associated with the token between `01` and `99`, with higher number indicating higher risk. A `00` value indicates the token was not scored by Visa.
    """
