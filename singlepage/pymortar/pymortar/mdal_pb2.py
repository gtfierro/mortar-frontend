# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mdal.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='mdal.proto',
  package='proto',
  syntax='proto3',
  serialized_pb=_b('\n\nmdal.proto\x12\x05proto\x1a\x1cgoogle/api/annotations.proto\"\xcd\x02\n\x10\x44\x61taQueryRequest\x12\x13\n\x0b\x63omposition\x18\x01 \x03(\t\x12=\n\x0b\x61ggregation\x18\x02 \x03(\x0b\x32(.proto.DataQueryRequest.AggregationEntry\x12\x39\n\tvariables\x18\x03 \x03(\x0b\x32&.proto.DataQueryRequest.VariablesEntry\x12\x1f\n\x04time\x18\x04 \x01(\x0b\x32\x11.proto.TimeParams\x1a\x46\n\x10\x41ggregationEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12!\n\x05value\x18\x02 \x01(\x0b\x32\x12.proto.Aggregation:\x02\x38\x01\x1a\x41\n\x0eVariablesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x1e\n\x05value\x18\x02 \x01(\x0b\x32\x0f.proto.Variable:\x02\x38\x01\"J\n\x08Variable\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x12\n\ndefinition\x18\x02 \x01(\t\x12\r\n\x05uuids\x18\x03 \x03(\t\x12\r\n\x05units\x18\x04 \x01(\t\"I\n\nTimeParams\x12\r\n\x05start\x18\x01 \x01(\t\x12\x0b\n\x03\x65nd\x18\x02 \x01(\t\x12\x0e\n\x06window\x18\x03 \x01(\t\x12\x0f\n\x07\x61ligned\x18\x04 \x01(\x08\",\n\x0b\x41ggregation\x12\x1d\n\x05\x66uncs\x18\x01 \x03(\x0e\x32\x0e.proto.AggFunc\"\x93\x04\n\x11\x44\x61taQueryResponse\x12*\n\x04rows\x18\x01 \x03(\x0b\x32\x1c.proto.DataQueryResponse.Row\x12\x36\n\x07mapping\x18\x02 \x03(\x0b\x32%.proto.DataQueryResponse.MappingEntry\x12-\n\x07\x63ontext\x18\x03 \x03(\x0b\x32\x1c.proto.DataQueryResponse.Row\x12\r\n\x05uuids\x18\x04 \x03(\t\x12\r\n\x05\x61rrow\x18\x05 \x01(\x0c\x12\r\n\x05\x65rror\x18\x06 \x01(\t\x12\r\n\x05times\x18\x07 \x03(\x03\x12\x33\n\x06values\x18\x08 \x03(\x0b\x32#.proto.DataQueryResponse.ValueArray\x1as\n\x03Row\x12\x0c\n\x04uuid\x18\x01 \x01(\x0c\x12\x32\n\x03row\x18\x02 \x03(\x0b\x32%.proto.DataQueryResponse.Row.RowEntry\x1a*\n\x08RowEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a\x17\n\x06VarMap\x12\r\n\x05uuids\x18\x01 \x03(\x0c\x1a\x1b\n\nValueArray\x12\r\n\x05value\x18\x01 \x03(\x01\x1aO\n\x0cMappingEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12.\n\x05value\x18\x02 \x01(\x0b\x32\x1f.proto.DataQueryResponse.VarMap:\x02\x38\x01*B\n\x07\x41ggFunc\x12\x07\n\x03RAW\x10\x00\x12\x08\n\x04MEAN\x10\x01\x12\x07\n\x03MIN\x10\x02\x12\x07\n\x03MAX\x10\x03\x12\t\n\x05\x43OUNT\x10\x04\x12\x07\n\x03SUM\x10\x05\x32\x61\n\x04MDAL\x12Y\n\tDataQuery\x12\x17.proto.DataQueryRequest\x1a\x18.proto.DataQueryResponse\"\x19\x82\xd3\xe4\x93\x02\x13\"\x0e/v1/mdal/query:\x01*b\x06proto3')
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,])

_AGGFUNC = _descriptor.EnumDescriptor(
  name='AggFunc',
  full_name='proto.AggFunc',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='RAW', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MEAN', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MIN', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MAX', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COUNT', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SUM', index=5, number=5,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1118,
  serialized_end=1184,
)
_sym_db.RegisterEnumDescriptor(_AGGFUNC)

AggFunc = enum_type_wrapper.EnumTypeWrapper(_AGGFUNC)
RAW = 0
MEAN = 1
MIN = 2
MAX = 3
COUNT = 4
SUM = 5



_DATAQUERYREQUEST_AGGREGATIONENTRY = _descriptor.Descriptor(
  name='AggregationEntry',
  full_name='proto.DataQueryRequest.AggregationEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='proto.DataQueryRequest.AggregationEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='proto.DataQueryRequest.AggregationEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=248,
  serialized_end=318,
)

_DATAQUERYREQUEST_VARIABLESENTRY = _descriptor.Descriptor(
  name='VariablesEntry',
  full_name='proto.DataQueryRequest.VariablesEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='proto.DataQueryRequest.VariablesEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='proto.DataQueryRequest.VariablesEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=320,
  serialized_end=385,
)

_DATAQUERYREQUEST = _descriptor.Descriptor(
  name='DataQueryRequest',
  full_name='proto.DataQueryRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='composition', full_name='proto.DataQueryRequest.composition', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='aggregation', full_name='proto.DataQueryRequest.aggregation', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='variables', full_name='proto.DataQueryRequest.variables', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='time', full_name='proto.DataQueryRequest.time', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_DATAQUERYREQUEST_AGGREGATIONENTRY, _DATAQUERYREQUEST_VARIABLESENTRY, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=52,
  serialized_end=385,
)


_VARIABLE = _descriptor.Descriptor(
  name='Variable',
  full_name='proto.Variable',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='proto.Variable.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='definition', full_name='proto.Variable.definition', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='uuids', full_name='proto.Variable.uuids', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='units', full_name='proto.Variable.units', index=3,
      number=4, type=9, cpp_type=9, label=1,
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
  serialized_start=387,
  serialized_end=461,
)


_TIMEPARAMS = _descriptor.Descriptor(
  name='TimeParams',
  full_name='proto.TimeParams',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='start', full_name='proto.TimeParams.start', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='end', full_name='proto.TimeParams.end', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='window', full_name='proto.TimeParams.window', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='aligned', full_name='proto.TimeParams.aligned', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=463,
  serialized_end=536,
)


_AGGREGATION = _descriptor.Descriptor(
  name='Aggregation',
  full_name='proto.Aggregation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='funcs', full_name='proto.Aggregation.funcs', index=0,
      number=1, type=14, cpp_type=8, label=3,
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
  serialized_start=538,
  serialized_end=582,
)


_DATAQUERYRESPONSE_ROW_ROWENTRY = _descriptor.Descriptor(
  name='RowEntry',
  full_name='proto.DataQueryResponse.Row.RowEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='proto.DataQueryResponse.Row.RowEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='proto.DataQueryResponse.Row.RowEntry.value', index=1,
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
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=939,
  serialized_end=981,
)

_DATAQUERYRESPONSE_ROW = _descriptor.Descriptor(
  name='Row',
  full_name='proto.DataQueryResponse.Row',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='uuid', full_name='proto.DataQueryResponse.Row.uuid', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='row', full_name='proto.DataQueryResponse.Row.row', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_DATAQUERYRESPONSE_ROW_ROWENTRY, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=866,
  serialized_end=981,
)

_DATAQUERYRESPONSE_VARMAP = _descriptor.Descriptor(
  name='VarMap',
  full_name='proto.DataQueryResponse.VarMap',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='uuids', full_name='proto.DataQueryResponse.VarMap.uuids', index=0,
      number=1, type=12, cpp_type=9, label=3,
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
  serialized_start=983,
  serialized_end=1006,
)

_DATAQUERYRESPONSE_VALUEARRAY = _descriptor.Descriptor(
  name='ValueArray',
  full_name='proto.DataQueryResponse.ValueArray',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='proto.DataQueryResponse.ValueArray.value', index=0,
      number=1, type=1, cpp_type=5, label=3,
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
  serialized_start=1008,
  serialized_end=1035,
)

_DATAQUERYRESPONSE_MAPPINGENTRY = _descriptor.Descriptor(
  name='MappingEntry',
  full_name='proto.DataQueryResponse.MappingEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='proto.DataQueryResponse.MappingEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='proto.DataQueryResponse.MappingEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1037,
  serialized_end=1116,
)

_DATAQUERYRESPONSE = _descriptor.Descriptor(
  name='DataQueryResponse',
  full_name='proto.DataQueryResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='rows', full_name='proto.DataQueryResponse.rows', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mapping', full_name='proto.DataQueryResponse.mapping', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='context', full_name='proto.DataQueryResponse.context', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='uuids', full_name='proto.DataQueryResponse.uuids', index=3,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='arrow', full_name='proto.DataQueryResponse.arrow', index=4,
      number=5, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='proto.DataQueryResponse.error', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='times', full_name='proto.DataQueryResponse.times', index=6,
      number=7, type=3, cpp_type=2, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='values', full_name='proto.DataQueryResponse.values', index=7,
      number=8, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_DATAQUERYRESPONSE_ROW, _DATAQUERYRESPONSE_VARMAP, _DATAQUERYRESPONSE_VALUEARRAY, _DATAQUERYRESPONSE_MAPPINGENTRY, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=585,
  serialized_end=1116,
)

_DATAQUERYREQUEST_AGGREGATIONENTRY.fields_by_name['value'].message_type = _AGGREGATION
_DATAQUERYREQUEST_AGGREGATIONENTRY.containing_type = _DATAQUERYREQUEST
_DATAQUERYREQUEST_VARIABLESENTRY.fields_by_name['value'].message_type = _VARIABLE
_DATAQUERYREQUEST_VARIABLESENTRY.containing_type = _DATAQUERYREQUEST
_DATAQUERYREQUEST.fields_by_name['aggregation'].message_type = _DATAQUERYREQUEST_AGGREGATIONENTRY
_DATAQUERYREQUEST.fields_by_name['variables'].message_type = _DATAQUERYREQUEST_VARIABLESENTRY
_DATAQUERYREQUEST.fields_by_name['time'].message_type = _TIMEPARAMS
_AGGREGATION.fields_by_name['funcs'].enum_type = _AGGFUNC
_DATAQUERYRESPONSE_ROW_ROWENTRY.containing_type = _DATAQUERYRESPONSE_ROW
_DATAQUERYRESPONSE_ROW.fields_by_name['row'].message_type = _DATAQUERYRESPONSE_ROW_ROWENTRY
_DATAQUERYRESPONSE_ROW.containing_type = _DATAQUERYRESPONSE
_DATAQUERYRESPONSE_VARMAP.containing_type = _DATAQUERYRESPONSE
_DATAQUERYRESPONSE_VALUEARRAY.containing_type = _DATAQUERYRESPONSE
_DATAQUERYRESPONSE_MAPPINGENTRY.fields_by_name['value'].message_type = _DATAQUERYRESPONSE_VARMAP
_DATAQUERYRESPONSE_MAPPINGENTRY.containing_type = _DATAQUERYRESPONSE
_DATAQUERYRESPONSE.fields_by_name['rows'].message_type = _DATAQUERYRESPONSE_ROW
_DATAQUERYRESPONSE.fields_by_name['mapping'].message_type = _DATAQUERYRESPONSE_MAPPINGENTRY
_DATAQUERYRESPONSE.fields_by_name['context'].message_type = _DATAQUERYRESPONSE_ROW
_DATAQUERYRESPONSE.fields_by_name['values'].message_type = _DATAQUERYRESPONSE_VALUEARRAY
DESCRIPTOR.message_types_by_name['DataQueryRequest'] = _DATAQUERYREQUEST
DESCRIPTOR.message_types_by_name['Variable'] = _VARIABLE
DESCRIPTOR.message_types_by_name['TimeParams'] = _TIMEPARAMS
DESCRIPTOR.message_types_by_name['Aggregation'] = _AGGREGATION
DESCRIPTOR.message_types_by_name['DataQueryResponse'] = _DATAQUERYRESPONSE
DESCRIPTOR.enum_types_by_name['AggFunc'] = _AGGFUNC
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DataQueryRequest = _reflection.GeneratedProtocolMessageType('DataQueryRequest', (_message.Message,), dict(

  AggregationEntry = _reflection.GeneratedProtocolMessageType('AggregationEntry', (_message.Message,), dict(
    DESCRIPTOR = _DATAQUERYREQUEST_AGGREGATIONENTRY,
    __module__ = 'mdal_pb2'
    # @@protoc_insertion_point(class_scope:proto.DataQueryRequest.AggregationEntry)
    ))
  ,

  VariablesEntry = _reflection.GeneratedProtocolMessageType('VariablesEntry', (_message.Message,), dict(
    DESCRIPTOR = _DATAQUERYREQUEST_VARIABLESENTRY,
    __module__ = 'mdal_pb2'
    # @@protoc_insertion_point(class_scope:proto.DataQueryRequest.VariablesEntry)
    ))
  ,
  DESCRIPTOR = _DATAQUERYREQUEST,
  __module__ = 'mdal_pb2'
  # @@protoc_insertion_point(class_scope:proto.DataQueryRequest)
  ))
_sym_db.RegisterMessage(DataQueryRequest)
_sym_db.RegisterMessage(DataQueryRequest.AggregationEntry)
_sym_db.RegisterMessage(DataQueryRequest.VariablesEntry)

Variable = _reflection.GeneratedProtocolMessageType('Variable', (_message.Message,), dict(
  DESCRIPTOR = _VARIABLE,
  __module__ = 'mdal_pb2'
  # @@protoc_insertion_point(class_scope:proto.Variable)
  ))
_sym_db.RegisterMessage(Variable)

TimeParams = _reflection.GeneratedProtocolMessageType('TimeParams', (_message.Message,), dict(
  DESCRIPTOR = _TIMEPARAMS,
  __module__ = 'mdal_pb2'
  # @@protoc_insertion_point(class_scope:proto.TimeParams)
  ))
_sym_db.RegisterMessage(TimeParams)

Aggregation = _reflection.GeneratedProtocolMessageType('Aggregation', (_message.Message,), dict(
  DESCRIPTOR = _AGGREGATION,
  __module__ = 'mdal_pb2'
  # @@protoc_insertion_point(class_scope:proto.Aggregation)
  ))
_sym_db.RegisterMessage(Aggregation)

DataQueryResponse = _reflection.GeneratedProtocolMessageType('DataQueryResponse', (_message.Message,), dict(

  Row = _reflection.GeneratedProtocolMessageType('Row', (_message.Message,), dict(

    RowEntry = _reflection.GeneratedProtocolMessageType('RowEntry', (_message.Message,), dict(
      DESCRIPTOR = _DATAQUERYRESPONSE_ROW_ROWENTRY,
      __module__ = 'mdal_pb2'
      # @@protoc_insertion_point(class_scope:proto.DataQueryResponse.Row.RowEntry)
      ))
    ,
    DESCRIPTOR = _DATAQUERYRESPONSE_ROW,
    __module__ = 'mdal_pb2'
    # @@protoc_insertion_point(class_scope:proto.DataQueryResponse.Row)
    ))
  ,

  VarMap = _reflection.GeneratedProtocolMessageType('VarMap', (_message.Message,), dict(
    DESCRIPTOR = _DATAQUERYRESPONSE_VARMAP,
    __module__ = 'mdal_pb2'
    # @@protoc_insertion_point(class_scope:proto.DataQueryResponse.VarMap)
    ))
  ,

  ValueArray = _reflection.GeneratedProtocolMessageType('ValueArray', (_message.Message,), dict(
    DESCRIPTOR = _DATAQUERYRESPONSE_VALUEARRAY,
    __module__ = 'mdal_pb2'
    # @@protoc_insertion_point(class_scope:proto.DataQueryResponse.ValueArray)
    ))
  ,

  MappingEntry = _reflection.GeneratedProtocolMessageType('MappingEntry', (_message.Message,), dict(
    DESCRIPTOR = _DATAQUERYRESPONSE_MAPPINGENTRY,
    __module__ = 'mdal_pb2'
    # @@protoc_insertion_point(class_scope:proto.DataQueryResponse.MappingEntry)
    ))
  ,
  DESCRIPTOR = _DATAQUERYRESPONSE,
  __module__ = 'mdal_pb2'
  # @@protoc_insertion_point(class_scope:proto.DataQueryResponse)
  ))
_sym_db.RegisterMessage(DataQueryResponse)
_sym_db.RegisterMessage(DataQueryResponse.Row)
_sym_db.RegisterMessage(DataQueryResponse.Row.RowEntry)
_sym_db.RegisterMessage(DataQueryResponse.VarMap)
_sym_db.RegisterMessage(DataQueryResponse.ValueArray)
_sym_db.RegisterMessage(DataQueryResponse.MappingEntry)


_DATAQUERYREQUEST_AGGREGATIONENTRY.has_options = True
_DATAQUERYREQUEST_AGGREGATIONENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
_DATAQUERYREQUEST_VARIABLESENTRY.has_options = True
_DATAQUERYREQUEST_VARIABLESENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
_DATAQUERYRESPONSE_ROW_ROWENTRY.has_options = True
_DATAQUERYRESPONSE_ROW_ROWENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
_DATAQUERYRESPONSE_MAPPINGENTRY.has_options = True
_DATAQUERYRESPONSE_MAPPINGENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))

_MDAL = _descriptor.ServiceDescriptor(
  name='MDAL',
  full_name='proto.MDAL',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=1186,
  serialized_end=1283,
  methods=[
  _descriptor.MethodDescriptor(
    name='DataQuery',
    full_name='proto.MDAL.DataQuery',
    index=0,
    containing_service=None,
    input_type=_DATAQUERYREQUEST,
    output_type=_DATAQUERYRESPONSE,
    options=_descriptor._ParseOptions(descriptor_pb2.MethodOptions(), _b('\202\323\344\223\002\023\"\016/v1/mdal/query:\001*')),
  ),
])
_sym_db.RegisterServiceDescriptor(_MDAL)

DESCRIPTOR.services_by_name['MDAL'] = _MDAL

# @@protoc_insertion_point(module_scope)