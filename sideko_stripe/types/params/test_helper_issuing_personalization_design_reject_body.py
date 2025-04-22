import pydantic
import typing
import typing_extensions

from .test_helper_issuing_personalization_design_reject_body_rejection_reasons import (
    TestHelperIssuingPersonalizationDesignRejectBodyRejectionReasons,
    _SerializerTestHelperIssuingPersonalizationDesignRejectBodyRejectionReasons,
)


class TestHelperIssuingPersonalizationDesignRejectBody(
    typing_extensions.TypedDict, total=False
):
    """
    TestHelperIssuingPersonalizationDesignRejectBody
    """

    expand: typing_extensions.NotRequired[typing.List[str]]
    """
    Specifies which fields in the response should be expanded.
    """

    rejection_reasons: typing_extensions.Required[
        TestHelperIssuingPersonalizationDesignRejectBodyRejectionReasons
    ]
    """
    The reason(s) the personalization design was rejected.
    """


class _SerializerTestHelperIssuingPersonalizationDesignRejectBody(pydantic.BaseModel):
    """
    Serializer for TestHelperIssuingPersonalizationDesignRejectBody handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
        extra="allow",
    )
    __pydantic_extra__: typing.Dict[str, typing.Any]

    expand: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="expand", default=None
    )
    rejection_reasons: _SerializerTestHelperIssuingPersonalizationDesignRejectBodyRejectionReasons = pydantic.Field(
        alias="rejection_reasons",
    )
