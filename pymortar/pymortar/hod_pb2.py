# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: hod.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='hod.proto',
  package='mdalgrpc',
  syntax='proto3',
  serialized_pb=_b('\n\thod.proto\x12\x08mdalgrpc\x1a\x1cgoogle/api/annotations.proto\"\x1d\n\x0cQueryRequest\x12\r\n\x05query\x18\x01 \x01(\t\"n\n\rQueryResponse\x12\x10\n\x08variable\x18\x01 \x03(\t\x12\x1b\n\x04rows\x18\x02 \x03(\x0b\x32\r.mdalgrpc.Row\x12\r\n\x05\x63ount\x18\x03 \x01(\x03\x12\x0f\n\x07\x65lapsed\x18\x04 \x01(\x03\x12\x0e\n\x06\x65rrors\x18\x05 \x03(\t\"\"\n\x03Row\x12\x1b\n\x04uris\x18\x01 \x03(\x0b\x32\r.mdalgrpc.URI\"\'\n\x03URI\x12\x11\n\tnamespace\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t2b\n\x05HodDB\x12Y\n\x0c\x45xecuteQuery\x12\x16.mdalgrpc.QueryRequest\x1a\x17.mdalgrpc.QueryResponse\"\x18\x82\xd3\xe4\x93\x02\x12\"\r/v1/hod/query:\x01*b\x06proto3')
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,])




_QUERYREQUEST = _descriptor.Descriptor(
  name='QueryRequest',
  full_name='mdalgrpc.QueryRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='query', full_name='mdalgrpc.QueryRequest.query', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=53,
  serialized_end=82,
)


_QUERYRESPONSE = _descriptor.Descriptor(
  name='QueryResponse',
  full_name='mdalgrpc.QueryResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='variable', full_name='mdalgrpc.QueryResponse.variable', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rows', full_name='mdalgrpc.QueryResponse.rows', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='count', full_name='mdalgrpc.QueryResponse.count', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='elapsed', full_name='mdalgrpc.QueryResponse.elapsed', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='errors', full_name='mdalgrpc.QueryResponse.errors', index=4,
      number=5, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=84,
  serialized_end=194,
)


_ROW = _descriptor.Descriptor(
  name='Row',
  full_name='mdalgrpc.Row',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='uris', full_name='mdalgrpc.Row.uris', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=196,
  serialized_end=230,
)


_URI = _descriptor.Descriptor(
  name='URI',
  full_name='mdalgrpc.URI',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='namespace', full_name='mdalgrpc.URI.namespace', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='mdalgrpc.URI.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=232,
  serialized_end=271,
)

_QUERYRESPONSE.fields_by_name['rows'].message_type = _ROW
_ROW.fields_by_name['uris'].message_type = _URI
DESCRIPTOR.message_types_by_name['QueryRequest'] = _QUERYREQUEST
DESCRIPTOR.message_types_by_name['QueryResponse'] = _QUERYRESPONSE
DESCRIPTOR.message_types_by_name['Row'] = _ROW
DESCRIPTOR.message_types_by_name['URI'] = _URI
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

QueryRequest = _reflection.GeneratedProtocolMessageType('QueryRequest', (_message.Message,), dict(
  DESCRIPTOR = _QUERYREQUEST,
  __module__ = 'hod_pb2'
  # @@protoc_insertion_point(class_scope:mdalgrpc.QueryRequest)
  ))
_sym_db.RegisterMessage(QueryRequest)

QueryResponse = _reflection.GeneratedProtocolMessageType('QueryResponse', (_message.Message,), dict(
  DESCRIPTOR = _QUERYRESPONSE,
  __module__ = 'hod_pb2'
  # @@protoc_insertion_point(class_scope:mdalgrpc.QueryResponse)
  ))
_sym_db.RegisterMessage(QueryResponse)

Row = _reflection.GeneratedProtocolMessageType('Row', (_message.Message,), dict(
  DESCRIPTOR = _ROW,
  __module__ = 'hod_pb2'
  # @@protoc_insertion_point(class_scope:mdalgrpc.Row)
  ))
_sym_db.RegisterMessage(Row)

URI = _reflection.GeneratedProtocolMessageType('URI', (_message.Message,), dict(
  DESCRIPTOR = _URI,
  __module__ = 'hod_pb2'
  # @@protoc_insertion_point(class_scope:mdalgrpc.URI)
  ))
_sym_db.RegisterMessage(URI)



_HODDB = _descriptor.ServiceDescriptor(
  name='HodDB',
  full_name='mdalgrpc.HodDB',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=273,
  serialized_end=371,
  methods=[
  _descriptor.MethodDescriptor(
    name='ExecuteQuery',
    full_name='mdalgrpc.HodDB.ExecuteQuery',
    index=0,
    containing_service=None,
    input_type=_QUERYREQUEST,
    output_type=_QUERYRESPONSE,
    options=_descriptor._ParseOptions(descriptor_pb2.MethodOptions(), _b('\202\323\344\223\002\022\"\r/v1/hod/query:\001*')),
  ),
])
_sym_db.RegisterServiceDescriptor(_HODDB)

DESCRIPTOR.services_by_name['HodDB'] = _HODDB

# @@protoc_insertion_point(module_scope)