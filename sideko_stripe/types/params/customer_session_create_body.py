import pydantic
import typing
import typing_extensions

from .customer_session_create_body_components import (
    CustomerSessionCreateBodyComponents,
    _SerializerCustomerSessionCreateBodyComponents,
)


class CustomerSessionCreateBody(typing_extensions.TypedDict, total=False):
    """
    CustomerSessionCreateBody
    """

    components: typing_extensions.Required[CustomerSessionCreateBodyComponents]
    """
    Configuration for each component. Exactly 1 component must be enabled.
    """

    customer: typing_extensions.Required[str]
    """
    The ID of an existing customer for which to create the Customer Session.
    """

    expand: typing_extensions.NotRequired[typing.List[str]]
    """
    Specifies which fields in the response should be expanded.
    """


class _SerializerCustomerSessionCreateBody(pydantic.BaseModel):
    """
    Serializer for CustomerSessionCreateBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, typing.Any]

    components: _SerializerCustomerSessionCreateBodyComponents = pydantic.Field(
        alias="components",
    )
    customer: str = pydantic.Field(
        alias="customer",
    )
    expand: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="expand", default=None
    )
