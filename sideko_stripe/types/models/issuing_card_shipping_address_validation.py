import pydantic
import typing
import typing_extensions

from .address import Address


class IssuingCardShippingAddressValidation(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    mode: typing_extensions.Literal[
        "disabled", "normalization_only", "validation_and_normalization"
    ] = pydantic.Field(
        alias="mode",
    )
    """
    The address validation capabilities to use.
    """
    normalized_address: typing.Optional[Address] = pydantic.Field(
        alias="normalized_address", default=None
    )
    result: typing.Optional[
        typing_extensions.Literal[
            "indeterminate", "likely_deliverable", "likely_undeliverable"
        ]
    ] = pydantic.Field(alias="result", default=None)
    """
    The validation result for the shipping address.
    """
