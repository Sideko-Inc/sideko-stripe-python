import pydantic
import typing


class SourceTypeCardPresent(pydantic.BaseModel):
    """
    SourceTypeCardPresent
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    application_cryptogram: typing.Optional[str] = pydantic.Field(
        alias="application_cryptogram", default=None
    )
    application_preferred_name: typing.Optional[str] = pydantic.Field(
        alias="application_preferred_name", default=None
    )
    authorization_code: typing.Optional[str] = pydantic.Field(
        alias="authorization_code", default=None
    )
    authorization_response_code: typing.Optional[str] = pydantic.Field(
        alias="authorization_response_code", default=None
    )
    brand: typing.Optional[str] = pydantic.Field(alias="brand", default=None)
    country: typing.Optional[str] = pydantic.Field(alias="country", default=None)
    cvm_type: typing.Optional[str] = pydantic.Field(alias="cvm_type", default=None)
    data_type: typing.Optional[str] = pydantic.Field(alias="data_type", default=None)
    dedicated_file_name: typing.Optional[str] = pydantic.Field(
        alias="dedicated_file_name", default=None
    )
    emv_auth_data: typing.Optional[str] = pydantic.Field(
        alias="emv_auth_data", default=None
    )
    evidence_customer_signature: typing.Optional[str] = pydantic.Field(
        alias="evidence_customer_signature", default=None
    )
    evidence_transaction_certificate: typing.Optional[str] = pydantic.Field(
        alias="evidence_transaction_certificate", default=None
    )
    exp_month: typing.Optional[int] = pydantic.Field(alias="exp_month", default=None)
    exp_year: typing.Optional[int] = pydantic.Field(alias="exp_year", default=None)
    fingerprint: typing.Optional[str] = pydantic.Field(
        alias="fingerprint", default=None
    )
    funding: typing.Optional[str] = pydantic.Field(alias="funding", default=None)
    last4: typing.Optional[str] = pydantic.Field(alias="last4", default=None)
    pos_device_id: typing.Optional[str] = pydantic.Field(
        alias="pos_device_id", default=None
    )
    pos_entry_mode: typing.Optional[str] = pydantic.Field(
        alias="pos_entry_mode", default=None
    )
    read_method: typing.Optional[str] = pydantic.Field(
        alias="read_method", default=None
    )
    reader: typing.Optional[str] = pydantic.Field(alias="reader", default=None)
    terminal_verification_results: typing.Optional[str] = pydantic.Field(
        alias="terminal_verification_results", default=None
    )
    transaction_status_information: typing.Optional[str] = pydantic.Field(
        alias="transaction_status_information", default=None
    )
