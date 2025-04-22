import pydantic
import typing
import typing_extensions


class ClimateOrderUpdateBodyBeneficiaryObj0(typing_extensions.TypedDict):
    """
    ClimateOrderUpdateBodyBeneficiaryObj0
    """

    public_name: typing_extensions.Required[typing.Union[str, str]]


class _SerializerClimateOrderUpdateBodyBeneficiaryObj0(pydantic.BaseModel):
    """
    Serializer for ClimateOrderUpdateBodyBeneficiaryObj0 handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    public_name: typing.Union[str, str] = pydantic.Field(
        alias="public_name",
    )
