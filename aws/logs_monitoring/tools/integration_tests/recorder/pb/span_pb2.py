# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: span.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\nspan.proto\x12\x02pb"\xcf\x02\n\x04Span\x12\x0f\n\x07service\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x10\n\x08resource\x18\x03 \x01(\t\x12\x0f\n\x07traceID\x18\x04 \x01(\x04\x12\x0e\n\x06spanID\x18\x05 \x01(\x04\x12\x10\n\x08parentID\x18\x06 \x01(\x04\x12\r\n\x05start\x18\x07 \x01(\x03\x12\x10\n\x08\x64uration\x18\x08 \x01(\x03\x12\r\n\x05\x65rror\x18\t \x01(\x05\x12 \n\x04meta\x18\n \x03(\x0b\x32\x12.pb.Span.MetaEntry\x12&\n\x07metrics\x18\x0b \x03(\x0b\x32\x15.pb.Span.MetricsEntry\x12\x0c\n\x04type\x18\x0c \x01(\t\x1a+\n\tMetaEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a.\n\x0cMetricsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x01:\x02\x38\x01\x62\x06proto3'
)


_SPAN = DESCRIPTOR.message_types_by_name["Span"]
_SPAN_METAENTRY = _SPAN.nested_types_by_name["MetaEntry"]
_SPAN_METRICSENTRY = _SPAN.nested_types_by_name["MetricsEntry"]
Span = _reflection.GeneratedProtocolMessageType(
    "Span",
    (_message.Message,),
    {
        "MetaEntry": _reflection.GeneratedProtocolMessageType(
            "MetaEntry",
            (_message.Message,),
            {
                "DESCRIPTOR": _SPAN_METAENTRY,
                "__module__": "span_pb2"
                # @@protoc_insertion_point(class_scope:pb.Span.MetaEntry)
            },
        ),
        "MetricsEntry": _reflection.GeneratedProtocolMessageType(
            "MetricsEntry",
            (_message.Message,),
            {
                "DESCRIPTOR": _SPAN_METRICSENTRY,
                "__module__": "span_pb2"
                # @@protoc_insertion_point(class_scope:pb.Span.MetricsEntry)
            },
        ),
        "DESCRIPTOR": _SPAN,
        "__module__": "span_pb2"
        # @@protoc_insertion_point(class_scope:pb.Span)
    },
)

_sym_db.RegisterMessage(Span)
_sym_db.RegisterMessage(Span.MetaEntry)
_sym_db.RegisterMessage(Span.MetricsEntry)

if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _SPAN_METAENTRY._options = None
    _SPAN_METAENTRY._serialized_options = b"8\001"
    _SPAN_METRICSENTRY._options = None
    _SPAN_METRICSENTRY._serialized_options = b"8\001"
    _SPAN._serialized_start = 19
    _SPAN._serialized_end = 354
    _SPAN_METAENTRY._serialized_start = 263
    _SPAN_METAENTRY._serialized_end = 306
    _SPAN_METRICSENTRY._serialized_start = 308
    _SPAN_METRICSENTRY._serialized_end = 354
# @@protoc_insertion_point(module_scope)
