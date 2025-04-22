import pydantic
import typing
import typing_extensions


class PortalCustomerUpdate(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    allowed_updates: typing.List[
        typing_extensions.Literal[
            "address", "email", "name", "phone", "shipping", "tax_id"
        ]
    ] = pydantic.Field(
        alias="allowed_updates",
    )
    """
    The types of customer updates that are supported. When empty, customers are not updateable.
    """
    enabled: bool = pydantic.Field(
        alias="enabled",
    )
    """
    Whether the feature is enabled.
    """
