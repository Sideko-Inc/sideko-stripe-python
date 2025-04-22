import pydantic
import typing_extensions


class BillingCreditGrantCreateBodyApplicabilityConfigScopePricesItem(
    typing_extensions.TypedDict
):
    """
    BillingCreditGrantCreateBodyApplicabilityConfigScopePricesItem
    """

    id: typing_extensions.Required[str]


class _SerializerBillingCreditGrantCreateBodyApplicabilityConfigScopePricesItem(
    pydantic.BaseModel
):
    """
    Serializer for BillingCreditGrantCreateBodyApplicabilityConfigScopePricesItem handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    id: str = pydantic.Field(
        alias="id",
    )
