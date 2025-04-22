import pydantic
import typing
import typing_extensions


class SetupIntentConfirmBodyPaymentMethodOptionsUsBankAccountMandateOptions(
    typing_extensions.TypedDict
):
    """
    SetupIntentConfirmBodyPaymentMethodOptionsUsBankAccountMandateOptions
    """

    collection_method: typing_extensions.NotRequired[typing_extensions.Literal["paper"]]


class _SerializerSetupIntentConfirmBodyPaymentMethodOptionsUsBankAccountMandateOptions(
    pydantic.BaseModel
):
    """
    Serializer for SetupIntentConfirmBodyPaymentMethodOptionsUsBankAccountMandateOptions handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    collection_method: typing.Optional[typing_extensions.Literal["paper"]] = (
        pydantic.Field(alias="collection_method", default=None)
    )
