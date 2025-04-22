import pydantic
import typing_extensions


class ClimateOrderCreateBodyBeneficiary(typing_extensions.TypedDict):
    """
    Publicly sharable reference for the end beneficiary of carbon removal. Assumed to be the Stripe account if not set.
    """

    public_name: typing_extensions.Required[str]


class _SerializerClimateOrderCreateBodyBeneficiary(pydantic.BaseModel):
    """
    Serializer for ClimateOrderCreateBodyBeneficiary handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    public_name: str = pydantic.Field(
        alias="public_name",
    )
