import pydantic
import typing
import typing_extensions


class PaymentMethodConfigResourceDisplayPreference(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    overridable: typing.Optional[bool] = pydantic.Field(
        alias="overridable", default=None
    )
    """
    For child configs, whether or not the account's preference will be observed. If `false`, the parent configuration's default is used.
    """
    preference: typing_extensions.Literal["none", "off", "on"] = pydantic.Field(
        alias="preference",
    )
    """
    The account's display preference.
    """
    value: typing_extensions.Literal["off", "on"] = pydantic.Field(
        alias="value",
    )
    """
    The effective display preference value.
    """
