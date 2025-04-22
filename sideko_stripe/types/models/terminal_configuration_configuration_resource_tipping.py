import pydantic
import typing

from .terminal_configuration_configuration_resource_currency_specific_config import (
    TerminalConfigurationConfigurationResourceCurrencySpecificConfig,
)


class TerminalConfigurationConfigurationResourceTipping(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    aud: typing.Optional[
        TerminalConfigurationConfigurationResourceCurrencySpecificConfig
    ] = pydantic.Field(alias="aud", default=None)
    cad: typing.Optional[
        TerminalConfigurationConfigurationResourceCurrencySpecificConfig
    ] = pydantic.Field(alias="cad", default=None)
    chf: typing.Optional[
        TerminalConfigurationConfigurationResourceCurrencySpecificConfig
    ] = pydantic.Field(alias="chf", default=None)
    czk: typing.Optional[
        TerminalConfigurationConfigurationResourceCurrencySpecificConfig
    ] = pydantic.Field(alias="czk", default=None)
    dkk: typing.Optional[
        TerminalConfigurationConfigurationResourceCurrencySpecificConfig
    ] = pydantic.Field(alias="dkk", default=None)
    eur: typing.Optional[
        TerminalConfigurationConfigurationResourceCurrencySpecificConfig
    ] = pydantic.Field(alias="eur", default=None)
    gbp: typing.Optional[
        TerminalConfigurationConfigurationResourceCurrencySpecificConfig
    ] = pydantic.Field(alias="gbp", default=None)
    hkd: typing.Optional[
        TerminalConfigurationConfigurationResourceCurrencySpecificConfig
    ] = pydantic.Field(alias="hkd", default=None)
    jpy: typing.Optional[
        TerminalConfigurationConfigurationResourceCurrencySpecificConfig
    ] = pydantic.Field(alias="jpy", default=None)
    myr: typing.Optional[
        TerminalConfigurationConfigurationResourceCurrencySpecificConfig
    ] = pydantic.Field(alias="myr", default=None)
    nok: typing.Optional[
        TerminalConfigurationConfigurationResourceCurrencySpecificConfig
    ] = pydantic.Field(alias="nok", default=None)
    nzd: typing.Optional[
        TerminalConfigurationConfigurationResourceCurrencySpecificConfig
    ] = pydantic.Field(alias="nzd", default=None)
    pln: typing.Optional[
        TerminalConfigurationConfigurationResourceCurrencySpecificConfig
    ] = pydantic.Field(alias="pln", default=None)
    sek: typing.Optional[
        TerminalConfigurationConfigurationResourceCurrencySpecificConfig
    ] = pydantic.Field(alias="sek", default=None)
    sgd: typing.Optional[
        TerminalConfigurationConfigurationResourceCurrencySpecificConfig
    ] = pydantic.Field(alias="sgd", default=None)
    usd: typing.Optional[
        TerminalConfigurationConfigurationResourceCurrencySpecificConfig
    ] = pydantic.Field(alias="usd", default=None)
