import pydantic
import typing


class SourceTypeCard(pydantic.BaseModel):
    """
    SourceTypeCard
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    address_line1_check: typing.Optional[str] = pydantic.Field(
        alias="address_line1_check", default=None
    )
    address_zip_check: typing.Optional[str] = pydantic.Field(
        alias="address_zip_check", default=None
    )
    brand: typing.Optional[str] = pydantic.Field(alias="brand", default=None)
    country: typing.Optional[str] = pydantic.Field(alias="country", default=None)
    cvc_check: typing.Optional[str] = pydantic.Field(alias="cvc_check", default=None)
    dynamic_last4: typing.Optional[str] = pydantic.Field(
        alias="dynamic_last4", default=None
    )
    exp_month: typing.Optional[int] = pydantic.Field(alias="exp_month", default=None)
    exp_year: typing.Optional[int] = pydantic.Field(alias="exp_year", default=None)
    fingerprint: typing.Optional[str] = pydantic.Field(
        alias="fingerprint", default=None
    )
    funding: typing.Optional[str] = pydantic.Field(alias="funding", default=None)
    last4: typing.Optional[str] = pydantic.Field(alias="last4", default=None)
    name: typing.Optional[str] = pydantic.Field(alias="name", default=None)
    three_d_secure: typing.Optional[str] = pydantic.Field(
        alias="three_d_secure", default=None
    )
    tokenization_method: typing.Optional[str] = pydantic.Field(
        alias="tokenization_method", default=None
    )
