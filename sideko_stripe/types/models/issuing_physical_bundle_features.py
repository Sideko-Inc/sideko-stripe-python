import pydantic
import typing_extensions


class IssuingPhysicalBundleFeatures(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    card_logo: typing_extensions.Literal["optional", "required", "unsupported"] = (
        pydantic.Field(
            alias="card_logo",
        )
    )
    """
    The policy for how to use card logo images in a card design with this physical bundle.
    """
    carrier_text: typing_extensions.Literal["optional", "required", "unsupported"] = (
        pydantic.Field(
            alias="carrier_text",
        )
    )
    """
    The policy for how to use carrier letter text in a card design with this physical bundle.
    """
    second_line: typing_extensions.Literal["optional", "required", "unsupported"] = (
        pydantic.Field(
            alias="second_line",
        )
    )
    """
    The policy for how to use a second line on a card with this physical bundle.
    """
