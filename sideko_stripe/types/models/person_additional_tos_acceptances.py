import pydantic
import typing

from .person_additional_tos_acceptance import PersonAdditionalTosAcceptance


class PersonAdditionalTosAcceptances(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    account: typing.Optional[PersonAdditionalTosAcceptance] = pydantic.Field(
        alias="account", default=None
    )
