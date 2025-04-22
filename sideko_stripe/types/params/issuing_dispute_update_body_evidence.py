import pydantic
import typing
import typing_extensions

from .issuing_dispute_update_body_evidence_canceled_obj0 import (
    IssuingDisputeUpdateBodyEvidenceCanceledObj0,
    _SerializerIssuingDisputeUpdateBodyEvidenceCanceledObj0,
)
from .issuing_dispute_update_body_evidence_duplicate_obj0 import (
    IssuingDisputeUpdateBodyEvidenceDuplicateObj0,
    _SerializerIssuingDisputeUpdateBodyEvidenceDuplicateObj0,
)
from .issuing_dispute_update_body_evidence_fraudulent_obj0 import (
    IssuingDisputeUpdateBodyEvidenceFraudulentObj0,
    _SerializerIssuingDisputeUpdateBodyEvidenceFraudulentObj0,
)
from .issuing_dispute_update_body_evidence_merchandise_not_as_described_obj0 import (
    IssuingDisputeUpdateBodyEvidenceMerchandiseNotAsDescribedObj0,
    _SerializerIssuingDisputeUpdateBodyEvidenceMerchandiseNotAsDescribedObj0,
)
from .issuing_dispute_update_body_evidence_no_valid_authorization_obj0 import (
    IssuingDisputeUpdateBodyEvidenceNoValidAuthorizationObj0,
    _SerializerIssuingDisputeUpdateBodyEvidenceNoValidAuthorizationObj0,
)
from .issuing_dispute_update_body_evidence_not_received_obj0 import (
    IssuingDisputeUpdateBodyEvidenceNotReceivedObj0,
    _SerializerIssuingDisputeUpdateBodyEvidenceNotReceivedObj0,
)
from .issuing_dispute_update_body_evidence_other_obj0 import (
    IssuingDisputeUpdateBodyEvidenceOtherObj0,
    _SerializerIssuingDisputeUpdateBodyEvidenceOtherObj0,
)
from .issuing_dispute_update_body_evidence_service_not_as_described_obj0 import (
    IssuingDisputeUpdateBodyEvidenceServiceNotAsDescribedObj0,
    _SerializerIssuingDisputeUpdateBodyEvidenceServiceNotAsDescribedObj0,
)


class IssuingDisputeUpdateBodyEvidence(typing_extensions.TypedDict):
    """
    Evidence provided for the dispute.
    """

    canceled: typing_extensions.NotRequired[
        typing.Union[IssuingDisputeUpdateBodyEvidenceCanceledObj0, str]
    ]

    duplicate: typing_extensions.NotRequired[
        typing.Union[IssuingDisputeUpdateBodyEvidenceDuplicateObj0, str]
    ]

    fraudulent: typing_extensions.NotRequired[
        typing.Union[IssuingDisputeUpdateBodyEvidenceFraudulentObj0, str]
    ]

    merchandise_not_as_described: typing_extensions.NotRequired[
        typing.Union[IssuingDisputeUpdateBodyEvidenceMerchandiseNotAsDescribedObj0, str]
    ]

    no_valid_authorization: typing_extensions.NotRequired[
        typing.Union[IssuingDisputeUpdateBodyEvidenceNoValidAuthorizationObj0, str]
    ]

    not_received: typing_extensions.NotRequired[
        typing.Union[IssuingDisputeUpdateBodyEvidenceNotReceivedObj0, str]
    ]

    other: typing_extensions.NotRequired[
        typing.Union[IssuingDisputeUpdateBodyEvidenceOtherObj0, str]
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
        typing.Union[IssuingDisputeUpdateBodyEvidenceServiceNotAsDescribedObj0, str]
    ]


class _SerializerIssuingDisputeUpdateBodyEvidence(pydantic.BaseModel):
    """
    Serializer for IssuingDisputeUpdateBodyEvidence handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    canceled: typing.Optional[
        typing.Union[_SerializerIssuingDisputeUpdateBodyEvidenceCanceledObj0, str]
    ] = pydantic.Field(alias="canceled", default=None)
    duplicate: typing.Optional[
        typing.Union[_SerializerIssuingDisputeUpdateBodyEvidenceDuplicateObj0, str]
    ] = pydantic.Field(alias="duplicate", default=None)
    fraudulent: typing.Optional[
        typing.Union[_SerializerIssuingDisputeUpdateBodyEvidenceFraudulentObj0, str]
    ] = pydantic.Field(alias="fraudulent", default=None)
    merchandise_not_as_described: typing.Optional[
        typing.Union[
            _SerializerIssuingDisputeUpdateBodyEvidenceMerchandiseNotAsDescribedObj0,
            str,
        ]
    ] = pydantic.Field(alias="merchandise_not_as_described", default=None)
    no_valid_authorization: typing.Optional[
        typing.Union[
            _SerializerIssuingDisputeUpdateBodyEvidenceNoValidAuthorizationObj0, str
        ]
    ] = pydantic.Field(alias="no_valid_authorization", default=None)
    not_received: typing.Optional[
        typing.Union[_SerializerIssuingDisputeUpdateBodyEvidenceNotReceivedObj0, str]
    ] = pydantic.Field(alias="not_received", default=None)
    other: typing.Optional[
        typing.Union[_SerializerIssuingDisputeUpdateBodyEvidenceOtherObj0, str]
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
            _SerializerIssuingDisputeUpdateBodyEvidenceServiceNotAsDescribedObj0, str
        ]
    ] = pydantic.Field(alias="service_not_as_described", default=None)
