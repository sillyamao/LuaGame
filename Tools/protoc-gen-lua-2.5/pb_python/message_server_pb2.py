# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: message_server.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import message_common_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='message_server.proto',
  package='pb',
  serialized_pb=_b('\n\x14message_server.proto\x12\x02pb\x1a\x14message_common.proto\"^\n\rTestMessageRe\x12\x33\n\x04type\x18\x01 \x01(\x0e\x32\x0c.pb.NET_TYPE:\x17NET_TYPE_TESTMESSAGE_RE\x12\n\n\x02id\x18\x02 \x01(\x05\x12\x0c\n\x04\x62uff\x18\x03 \x01(\x0c')
  ,
  dependencies=[message_common_pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_TESTMESSAGERE = _descriptor.Descriptor(
  name='TestMessageRe',
  full_name='pb.TestMessageRe',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='pb.TestMessageRe.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=5,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='id', full_name='pb.TestMessageRe.id', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='buff', full_name='pb.TestMessageRe.buff', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=50,
  serialized_end=144,
)

_TESTMESSAGERE.fields_by_name['type'].enum_type = message_common_pb2._NET_TYPE
DESCRIPTOR.message_types_by_name['TestMessageRe'] = _TESTMESSAGERE

TestMessageRe = _reflection.GeneratedProtocolMessageType('TestMessageRe', (_message.Message,), dict(
  DESCRIPTOR = _TESTMESSAGERE,
  __module__ = 'message_server_pb2'
  # @@protoc_insertion_point(class_scope:pb.TestMessageRe)
  ))
_sym_db.RegisterMessage(TestMessageRe)


# @@protoc_insertion_point(module_scope)
