import pydantic
import typing


class SourceTypeKlarna(pydantic.BaseModel):
    """
    SourceTypeKlarna
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    background_image_url: typing.Optional[str] = pydantic.Field(
        alias="background_image_url", default=None
    )
    client_token: typing.Optional[str] = pydantic.Field(
        alias="client_token", default=None
    )
    first_name: typing.Optional[str] = pydantic.Field(alias="first_name", default=None)
    last_name: typing.Optional[str] = pydantic.Field(alias="last_name", default=None)
    locale: typing.Optional[str] = pydantic.Field(alias="locale", default=None)
    logo_url: typing.Optional[str] = pydantic.Field(alias="logo_url", default=None)
    page_title: typing.Optional[str] = pydantic.Field(alias="page_title", default=None)
    pay_later_asset_urls_descriptive: typing.Optional[str] = pydantic.Field(
        alias="pay_later_asset_urls_descriptive", default=None
    )
    pay_later_asset_urls_standard: typing.Optional[str] = pydantic.Field(
        alias="pay_later_asset_urls_standard", default=None
    )
    pay_later_name: typing.Optional[str] = pydantic.Field(
        alias="pay_later_name", default=None
    )
    pay_later_redirect_url: typing.Optional[str] = pydantic.Field(
        alias="pay_later_redirect_url", default=None
    )
    pay_now_asset_urls_descriptive: typing.Optional[str] = pydantic.Field(
        alias="pay_now_asset_urls_descriptive", default=None
    )
    pay_now_asset_urls_standard: typing.Optional[str] = pydantic.Field(
        alias="pay_now_asset_urls_standard", default=None
    )
    pay_now_name: typing.Optional[str] = pydantic.Field(
        alias="pay_now_name", default=None
    )
    pay_now_redirect_url: typing.Optional[str] = pydantic.Field(
        alias="pay_now_redirect_url", default=None
    )
    pay_over_time_asset_urls_descriptive: typing.Optional[str] = pydantic.Field(
        alias="pay_over_time_asset_urls_descriptive", default=None
    )
    pay_over_time_asset_urls_standard: typing.Optional[str] = pydantic.Field(
        alias="pay_over_time_asset_urls_standard", default=None
    )
    pay_over_time_name: typing.Optional[str] = pydantic.Field(
        alias="pay_over_time_name", default=None
    )
    pay_over_time_redirect_url: typing.Optional[str] = pydantic.Field(
        alias="pay_over_time_redirect_url", default=None
    )
    payment_method_categories: typing.Optional[str] = pydantic.Field(
        alias="payment_method_categories", default=None
    )
    purchase_country: typing.Optional[str] = pydantic.Field(
        alias="purchase_country", default=None
    )
    purchase_type: typing.Optional[str] = pydantic.Field(
        alias="purchase_type", default=None
    )
    redirect_url: typing.Optional[str] = pydantic.Field(
        alias="redirect_url", default=None
    )
    shipping_delay: typing.Optional[int] = pydantic.Field(
        alias="shipping_delay", default=None
    )
    shipping_first_name: typing.Optional[str] = pydantic.Field(
        alias="shipping_first_name", default=None
    )
    shipping_last_name: typing.Optional[str] = pydantic.Field(
        alias="shipping_last_name", default=None
    )
