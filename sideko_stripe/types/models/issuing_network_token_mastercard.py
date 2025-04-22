import pydantic
import typing


class IssuingNetworkTokenMastercard(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    card_reference_id: typing.Optional[str] = pydantic.Field(
        alias="card_reference_id", default=None
    )
    """
    A unique reference ID from MasterCard to represent the card account number.
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
    The ID of the entity requesting tokenization, specific to MasterCard.
    """
    token_requestor_name: typing.Optional[str] = pydantic.Field(
        alias="token_requestor_name", default=None
    )
    """
    The name of the entity requesting tokenization, if known. This is directly provided from MasterCard.
    """
