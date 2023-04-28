# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: FresnoDailyNews.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='FresnoDailyNews.proto',
  package='fresnodailynews',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x15\x46resnoDailyNews.proto\x12\x0f\x66resnodailynews\")\n\x16\x45xtractKeywordsRequest\x12\x0f\n\x07message\x18\x01 \x01(\t\"(\n\x17\x45xtractKeywordsResponse\x12\r\n\x05reply\x18\x01 \x01(\t2x\n\x0f\x46resnoDailyNews\x12\x65\n\x0e\x45xtractKeyword\x12\'.fresnodailynews.ExtractKeywordsRequest\x1a(.fresnodailynews.ExtractKeywordsResponse\"\x00\x62\x06proto3'
)




_EXTRACTKEYWORDSREQUEST = _descriptor.Descriptor(
  name='ExtractKeywordsRequest',
  full_name='fresnodailynews.ExtractKeywordsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='fresnodailynews.ExtractKeywordsRequest.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=42,
  serialized_end=83,
)


_EXTRACTKEYWORDSRESPONSE = _descriptor.Descriptor(
  name='ExtractKeywordsResponse',
  full_name='fresnodailynews.ExtractKeywordsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='reply', full_name='fresnodailynews.ExtractKeywordsResponse.reply', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=85,
  serialized_end=125,
)

DESCRIPTOR.message_types_by_name['ExtractKeywordsRequest'] = _EXTRACTKEYWORDSREQUEST
DESCRIPTOR.message_types_by_name['ExtractKeywordsResponse'] = _EXTRACTKEYWORDSRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ExtractKeywordsRequest = _reflection.GeneratedProtocolMessageType('ExtractKeywordsRequest', (_message.Message,), {
  'DESCRIPTOR' : _EXTRACTKEYWORDSREQUEST,
  '__module__' : 'FresnoDailyNews_pb2'
  # @@protoc_insertion_point(class_scope:fresnodailynews.ExtractKeywordsRequest)
  })
_sym_db.RegisterMessage(ExtractKeywordsRequest)

ExtractKeywordsResponse = _reflection.GeneratedProtocolMessageType('ExtractKeywordsResponse', (_message.Message,), {
  'DESCRIPTOR' : _EXTRACTKEYWORDSRESPONSE,
  '__module__' : 'FresnoDailyNews_pb2'
  # @@protoc_insertion_point(class_scope:fresnodailynews.ExtractKeywordsResponse)
  })
_sym_db.RegisterMessage(ExtractKeywordsResponse)



_FRESNODAILYNEWS = _descriptor.ServiceDescriptor(
  name='FresnoDailyNews',
  full_name='fresnodailynews.FresnoDailyNews',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=127,
  serialized_end=247,
  methods=[
  _descriptor.MethodDescriptor(
    name='ExtractKeyword',
    full_name='fresnodailynews.FresnoDailyNews.ExtractKeyword',
    index=0,
    containing_service=None,
    input_type=_EXTRACTKEYWORDSREQUEST,
    output_type=_EXTRACTKEYWORDSRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_FRESNODAILYNEWS)

DESCRIPTOR.services_by_name['FresnoDailyNews'] = _FRESNODAILYNEWS

# @@protoc_insertion_point(module_scope)
