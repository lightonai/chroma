from chromadb.proto import chroma_pb2 as _chroma_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import (
    ClassVar as _ClassVar,
    Iterable as _Iterable,
    Mapping as _Mapping,
    Optional as _Optional,
    Union as _Union,
)

DESCRIPTOR: _descriptor.FileDescriptor

class PushLogsRequest(_message.Message):
    __slots__ = ["collection_id", "records"]
    COLLECTION_ID_FIELD_NUMBER: _ClassVar[int]
    RECORDS_FIELD_NUMBER: _ClassVar[int]
    collection_id: str
    records: _containers.RepeatedCompositeFieldContainer[
        _chroma_pb2.SubmitEmbeddingRecord
    ]
    def __init__(
        self,
        collection_id: _Optional[str] = ...,
        records: _Optional[
            _Iterable[_Union[_chroma_pb2.SubmitEmbeddingRecord, _Mapping]]
        ] = ...,
    ) -> None: ...

class PushLogsResponse(_message.Message):
    __slots__ = ["record_count"]
    RECORD_COUNT_FIELD_NUMBER: _ClassVar[int]
    record_count: int
    def __init__(self, record_count: _Optional[int] = ...) -> None: ...

class PullLogsRequest(_message.Message):
    __slots__ = ["collection_id", "start_from_id", "batch_size"]
    COLLECTION_ID_FIELD_NUMBER: _ClassVar[int]
    START_FROM_ID_FIELD_NUMBER: _ClassVar[int]
    BATCH_SIZE_FIELD_NUMBER: _ClassVar[int]
    collection_id: str
    start_from_id: int
    batch_size: int
    def __init__(
        self,
        collection_id: _Optional[str] = ...,
        start_from_id: _Optional[int] = ...,
        batch_size: _Optional[int] = ...,
    ) -> None: ...

class PullLogsResponse(_message.Message):
    __slots__ = ["records"]
    RECORDS_FIELD_NUMBER: _ClassVar[int]
    records: _containers.RepeatedCompositeFieldContainer[
        _chroma_pb2.SubmitEmbeddingRecord
    ]
    def __init__(
        self,
        records: _Optional[
            _Iterable[_Union[_chroma_pb2.SubmitEmbeddingRecord, _Mapping]]
        ] = ...,
    ) -> None: ...

class CollectionInfo(_message.Message):
    __slots__ = ["collection_id", "first_log_id", "first_log_id_ts"]
    COLLECTION_ID_FIELD_NUMBER: _ClassVar[int]
    FIRST_LOG_ID_FIELD_NUMBER: _ClassVar[int]
    FIRST_LOG_ID_TS_FIELD_NUMBER: _ClassVar[int]
    collection_id: str
    first_log_id: int
    first_log_id_ts: int
    def __init__(
        self,
        collection_id: _Optional[str] = ...,
        first_log_id: _Optional[int] = ...,
        first_log_id_ts: _Optional[int] = ...,
    ) -> None: ...

class GetAllCollectionInfoToCompactRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class GetAllCollectionInfoToCompactResponse(_message.Message):
    __slots__ = ["all_collection_info"]
    ALL_COLLECTION_INFO_FIELD_NUMBER: _ClassVar[int]
    all_collection_info: _containers.RepeatedCompositeFieldContainer[CollectionInfo]
    def __init__(
        self,
        all_collection_info: _Optional[
            _Iterable[_Union[CollectionInfo, _Mapping]]
        ] = ...,
    ) -> None: ...
