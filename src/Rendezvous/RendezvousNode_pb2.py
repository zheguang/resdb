# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: RendezvousNode.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='RendezvousNode.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x14RendezvousNode.proto\":\n\x0eNodeGetRequest\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\x0b\n\x03key\x18\x02 \x01(\t\x12\r\n\x05value\x18\x03 \x01(\t\"\x0e\n\x0cNodeGetReply\"&\n\x17NodeHashValueForRequest\x12\x0b\n\x03key\x18\x01 \x01(\t\"*\n\x15NodeHashValueForReply\x12\x11\n\thashValue\x18\x01 \x01(\t2\x8b\x01\n\x0eRendezvousNode\x12H\n\x12hash_value_for_key\x12\x18.NodeHashValueForRequest\x1a\x16.NodeHashValueForReply\"\x00\x12/\n\x0bget_request\x12\x0f.NodeGetRequest\x1a\r.NodeGetReply\"\x00\x62\x06proto3'
)




_NODEGETREQUEST = _descriptor.Descriptor(
  name='NodeGetRequest',
  full_name='NodeGetRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='NodeGetRequest.type', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='key', full_name='NodeGetRequest.key', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='NodeGetRequest.value', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  serialized_start=24,
  serialized_end=82,
)


_NODEGETREPLY = _descriptor.Descriptor(
  name='NodeGetReply',
  full_name='NodeGetReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
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
  serialized_start=84,
  serialized_end=98,
)


_NODEHASHVALUEFORREQUEST = _descriptor.Descriptor(
  name='NodeHashValueForRequest',
  full_name='NodeHashValueForRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='NodeHashValueForRequest.key', index=0,
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
  serialized_start=100,
  serialized_end=138,
)


_NODEHASHVALUEFORREPLY = _descriptor.Descriptor(
  name='NodeHashValueForReply',
  full_name='NodeHashValueForReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='hashValue', full_name='NodeHashValueForReply.hashValue', index=0,
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
  serialized_start=140,
  serialized_end=182,
)

DESCRIPTOR.message_types_by_name['NodeGetRequest'] = _NODEGETREQUEST
DESCRIPTOR.message_types_by_name['NodeGetReply'] = _NODEGETREPLY
DESCRIPTOR.message_types_by_name['NodeHashValueForRequest'] = _NODEHASHVALUEFORREQUEST
DESCRIPTOR.message_types_by_name['NodeHashValueForReply'] = _NODEHASHVALUEFORREPLY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

NodeGetRequest = _reflection.GeneratedProtocolMessageType('NodeGetRequest', (_message.Message,), {
  'DESCRIPTOR' : _NODEGETREQUEST,
  '__module__' : 'RendezvousNode_pb2'
  # @@protoc_insertion_point(class_scope:NodeGetRequest)
  })
_sym_db.RegisterMessage(NodeGetRequest)

NodeGetReply = _reflection.GeneratedProtocolMessageType('NodeGetReply', (_message.Message,), {
  'DESCRIPTOR' : _NODEGETREPLY,
  '__module__' : 'RendezvousNode_pb2'
  # @@protoc_insertion_point(class_scope:NodeGetReply)
  })
_sym_db.RegisterMessage(NodeGetReply)

NodeHashValueForRequest = _reflection.GeneratedProtocolMessageType('NodeHashValueForRequest', (_message.Message,), {
  'DESCRIPTOR' : _NODEHASHVALUEFORREQUEST,
  '__module__' : 'RendezvousNode_pb2'
  # @@protoc_insertion_point(class_scope:NodeHashValueForRequest)
  })
_sym_db.RegisterMessage(NodeHashValueForRequest)

NodeHashValueForReply = _reflection.GeneratedProtocolMessageType('NodeHashValueForReply', (_message.Message,), {
  'DESCRIPTOR' : _NODEHASHVALUEFORREPLY,
  '__module__' : 'RendezvousNode_pb2'
  # @@protoc_insertion_point(class_scope:NodeHashValueForReply)
  })
_sym_db.RegisterMessage(NodeHashValueForReply)



_RENDEZVOUSNODE = _descriptor.ServiceDescriptor(
  name='RendezvousNode',
  full_name='RendezvousNode',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=185,
  serialized_end=324,
  methods=[
  _descriptor.MethodDescriptor(
    name='hash_value_for_key',
    full_name='RendezvousNode.hash_value_for_key',
    index=0,
    containing_service=None,
    input_type=_NODEHASHVALUEFORREQUEST,
    output_type=_NODEHASHVALUEFORREPLY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='get_request',
    full_name='RendezvousNode.get_request',
    index=1,
    containing_service=None,
    input_type=_NODEGETREQUEST,
    output_type=_NODEGETREPLY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_RENDEZVOUSNODE)

DESCRIPTOR.services_by_name['RendezvousNode'] = _RENDEZVOUSNODE

# @@protoc_insertion_point(module_scope)