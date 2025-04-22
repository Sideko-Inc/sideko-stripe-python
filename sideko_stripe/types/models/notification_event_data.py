import pydantic
import typing


class NotificationEventData(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    object: typing.Dict[str, typing.Any] = pydantic.Field(
        alias="object",
    )
    """
    Object containing the API resource relevant to the event. For example, an `invoice.created` event will have a full [invoice object](https://stripe.com/docs/api#invoice_object) as the value of the object key.
    """
    previous_attributes: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="previous_attributes", default=None
    )
    """
    Object containing the names of the updated attributes and their values prior to the event (only included in events of type `*.updated`). If an array attribute has any updated elements, this object contains the entire array. In Stripe API versions 2017-04-06 or earlier, an updated array attribute in this object includes only the updated array elements.
    """
