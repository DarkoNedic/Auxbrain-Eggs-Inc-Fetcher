# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: post_data.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='post_data.proto',
  package='',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=b'\n\x0fpost_data.proto\"3\n\x08userdata\x12\x0f\n\x07user_id\x18\x01 \x02(\t\x12\n\n\x02\x66\x31\x18\x02 \x01(\x08\x12\n\n\x02\x66\x32\x18\x03 \x01(\x08'
)




_USERDATA = _descriptor.Descriptor(
  name='userdata',
  full_name='userdata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_id', full_name='userdata.user_id', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='f1', full_name='userdata.f1', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='f2', full_name='userdata.f2', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=19,
  serialized_end=70,
)

DESCRIPTOR.message_types_by_name['userdata'] = _USERDATA
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

userdata = _reflection.GeneratedProtocolMessageType('userdata', (_message.Message,), {
  'DESCRIPTOR' : _USERDATA,
  '__module__' : 'post_data_pb2'
  # @@protoc_insertion_point(class_scope:userdata)
  })
_sym_db.RegisterMessage(userdata)


# @@protoc_insertion_point(module_scope)
