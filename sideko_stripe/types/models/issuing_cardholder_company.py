import pydantic


class IssuingCardholderCompany(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    tax_id_provided: bool = pydantic.Field(
        alias="tax_id_provided",
    )
    """
    Whether the company's business ID number was provided.
    """
