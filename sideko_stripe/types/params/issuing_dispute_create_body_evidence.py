import pydantic
import typing
import typing_extensions

from .issuing_dispute_create_body_evidence_canceled_obj0 import (
    IssuingDisputeCreateBodyEvidenceCanceledObj0,
    _SerializerIssuingDisputeCreateBodyEvidenceCanceledObj0,
)
from .issuing_dispute_create_body_evidence_duplicate_obj0 import (
    IssuingDisputeCreateBodyEvidenceDuplicateObj0,
    _SerializerIssuingDisputeCreateBodyEvidenceDuplicateObj0,
)
from .issuing_dispute_create_body_evidence_fraudulent_obj0 import (
    IssuingDisputeCreateBodyEvidenceFraudulentObj0,
    _SerializerIssuingDisputeCreateBodyEvidenceFraudulentObj0,
)
from .issuing_dispute_create_body_evidence_merchandise_not_as_described_obj0 import (
    IssuingDisputeCreateBodyEvidenceMerchandiseNotAsDescribedObj0,
    _SerializerIssuingDisputeCreateBodyEvidenceMerchandiseNotAsDescribedObj0,
)
from .issuing_dispute_create_body_evidence_no_valid_authorization_obj0 import (
    IssuingDisputeCreateBodyEvidenceNoValidAuthorizationObj0,
    _SerializerIssuingDisputeCreateBodyEvidenceNoValidAuthorizationObj0,
)
from .issuing_dispute_create_body_evidence_not_received_obj0 import (
    IssuingDisputeCreateBodyEvidenceNotReceivedObj0,
    _SerializerIssuingDisputeCreateBodyEvidenceNotReceivedObj0,
)
from .issuing_dispute_create_body_evidence_other_obj0 import (
    IssuingDisputeCreateBodyEvidenceOtherObj0,
    _SerializerIssuingDisputeCreateBodyEvidenceOtherObj0,
)
from .issuing_dispute_create_body_evidence_service_not_as_described_obj0 import (
    IssuingDisputeCreateBodyEvidenceServiceNotAsDescribedObj0,
    _SerializerIssuingDisputeCreateBodyEvidenceServiceNotAsDescribedObj0,
)


class IssuingDisputeCreateBodyEvidence(typing_extensions.TypedDict):
    """
    Evidence provided for the dispute.
    """

    canceled: typing_extensions.NotRequired[
        typing.Union[IssuingDisputeCreateBodyEvidenceCanceledObj0, str]
    ]

    duplicate: typing_extensions.NotRequired[
        typing.Union[IssuingDisputeCreateBodyEvidenceDuplicateObj0, str]
    ]

    fraudulent: typing_extensions.NotRequired[
        typing.Union[IssuingDisputeCreateBodyEvidenceFraudulentObj0, str]
    ]

    merchandise_not_as_described: typing_extensions.NotRequired[
        typing.Union[IssuingDisputeCreateBodyEvidenceMerchandiseNotAsDescribedObj0, str]
    ]

    no_valid_authorization: typing_extensions.NotRequired[
        typing.Union[IssuingDisputeCreateBodyEvidenceNoValidAuthorizationObj0, str]
    ]

    not_received: typing_extensions.NotRequired[
        typing.Union[IssuingDisputeCreateBodyEvidenceNotReceivedObj0, str]
    ]

    other: typing_extensions.NotRequired[
        typing.Union[IssuingDisputeCreateBodyEvidenceOtherObj0, str]
    ]

    reason: typing_extensions.NotRequired[
        typing_extensions.Literal[
            "canceled",
            "duplicate",
            "fraudulent",
            "merchandise_not_as_described",
            "no_valid_authorization",
            "not_received",
            "other",
            "service_not_as_described",
        ]
    ]

    service_not_as_described: typing_extensions.NotRequired[
        typing.Union[IssuingDisputeCreateBodyEvidenceServiceNotAsDescribedObj0, str]
    ]


class _SerializerIssuingDisputeCreateBodyEvidence(pydantic.BaseModel):
    """
    Serializer for IssuingDisputeCreateBodyEvidence handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    canceled: typing.Optional[
        typing.Union[_SerializerIssuingDisputeCreateBodyEvidenceCanceledObj0, str]
    ] = pydantic.Field(alias="canceled", default=None)
    duplicate: typing.Optional[
        typing.Union[_SerializerIssuingDisputeCreateBodyEvidenceDuplicateObj0, str]
    ] = pydantic.Field(alias="duplicate", default=None)
    fraudulent: typing.Optional[
        typing.Union[_SerializerIssuingDisputeCreateBodyEvidenceFraudulentObj0, str]
    ] = pydantic.Field(alias="fraudulent", default=None)
    merchandise_not_as_described: typing.Optional[
        typing.Union[
            _SerializerIssuingDisputeCreateBodyEvidenceMerchandiseNotAsDescribedObj0,
            str,
        ]
    ] = pydantic.Field(alias="merchandise_not_as_described", default=None)
    no_valid_authorization: typing.Optional[
        typing.Union[
            _SerializerIssuingDisputeCreateBodyEvidenceNoValidAuthorizationObj0, str
        ]
    ] = pydantic.Field(alias="no_valid_authorization", default=None)
    not_received: typing.Optional[
        typing.Union[_SerializerIssuingDisputeCreateBodyEvidenceNotReceivedObj0, str]
    ] = pydantic.Field(alias="not_received", default=None)
    other: typing.Optional[
        typing.Union[_SerializerIssuingDisputeCreateBodyEvidenceOtherObj0, str]
    ] = pydantic.Field(alias="other", default=None)
    reason: typing.Optional[
        typing_extensions.Literal[
            "canceled",
            "duplicate",
            "fraudulent",
            "merchandise_not_as_described",
            "no_valid_authorization",
            "not_received",
            "other",
            "service_not_as_described",
        ]
    ] = pydantic.Field(alias="reason", default=None)
    service_not_as_described: typing.Optional[
        typing.Union[
            _SerializerIssuingDisputeCreateBodyEvidenceServiceNotAsDescribedObj0, str
        ]
    ] = pydantic.Field(alias="service_not_as_described", default=None)
