import pydantic
import typing
import typing_extensions


class MandateUsBankAccount(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    collection_method: typing.Optional[typing_extensions.Literal["paper"]] = (
        pydantic.Field(alias="collection_method", default=None)
    )
    """
    Mandate collection method
    """
