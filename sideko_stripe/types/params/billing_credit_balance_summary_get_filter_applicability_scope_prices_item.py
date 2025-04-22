import pydantic
import typing_extensions


class BillingCreditBalanceSummaryGetFilterApplicabilityScopePricesItem(
    typing_extensions.TypedDict
):
    """
    BillingCreditBalanceSummaryGetFilterApplicabilityScopePricesItem
    """

    id: typing_extensions.Required[str]


class _SerializerBillingCreditBalanceSummaryGetFilterApplicabilityScopePricesItem(
    pydantic.BaseModel
):
    """
    Serializer for BillingCreditBalanceSummaryGetFilterApplicabilityScopePricesItem handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    id: str = pydantic.Field(
        alias="id",
    )
