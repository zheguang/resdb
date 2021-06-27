# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: RendezvousHashing.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='RendezvousHashing.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x17RendezvousHashing.proto\"(\n\x19RendezvousFindNodeRequest\x12\x0b\n\x03key\x18\x01 \x01(\t\";\n\x17RendezvousFindNodeReply\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x12\n\nip_address\x18\x02 \x01(\t2d\n\x11RendezvousHashing\x12O\n\x15\x66ind_responsible_node\x12\x1a.RendezvousFindNodeRequest\x1a\x18.RendezvousFindNodeReply\"\x00\x62\x06proto3'
)




_RENDEZVOUSFINDNODEREQUEST = _descriptor.Descriptor(
  name='RendezvousFindNodeRequest',
  full_name='RendezvousFindNodeRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='RendezvousFindNodeRequest.key', index=0,
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
  serialized_start=27,
  serialized_end=67,
)


_RENDEZVOUSFINDNODEREPLY = _descriptor.Descriptor(
  name='RendezvousFindNodeReply',
  full_name='RendezvousFindNodeReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='RendezvousFindNodeReply.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ip_address', full_name='RendezvousFindNodeReply.ip_address', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=69,
  serialized_end=128,
)

DESCRIPTOR.message_types_by_name['RendezvousFindNodeRequest'] = _RENDEZVOUSFINDNODEREQUEST
DESCRIPTOR.message_types_by_name['RendezvousFindNodeReply'] = _RENDEZVOUSFINDNODEREPLY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RendezvousFindNodeRequest = _reflection.GeneratedProtocolMessageType('RendezvousFindNodeRequest', (_message.Message,), {
  'DESCRIPTOR' : _RENDEZVOUSFINDNODEREQUEST,
  '__module__' : 'RendezvousHashing_pb2'
  # @@protoc_insertion_point(class_scope:RendezvousFindNodeRequest)
  })
_sym_db.RegisterMessage(RendezvousFindNodeRequest)

RendezvousFindNodeReply = _reflection.GeneratedProtocolMessageType('RendezvousFindNodeReply', (_message.Message,), {
  'DESCRIPTOR' : _RENDEZVOUSFINDNODEREPLY,
  '__module__' : 'RendezvousHashing_pb2'
  # @@protoc_insertion_point(class_scope:RendezvousFindNodeReply)
  })
_sym_db.RegisterMessage(RendezvousFindNodeReply)



_RENDEZVOUSHASHING = _descriptor.ServiceDescriptor(
  name='RendezvousHashing',
  full_name='RendezvousHashing',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=130,
  serialized_end=230,
  methods=[
  _descriptor.MethodDescriptor(
    name='find_responsible_node',
    full_name='RendezvousHashing.find_responsible_node',
    index=0,
    containing_service=None,
    input_type=_RENDEZVOUSFINDNODEREQUEST,
    output_type=_RENDEZVOUSFINDNODEREPLY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_RENDEZVOUSHASHING)

DESCRIPTOR.services_by_name['RendezvousHashing'] = _RENDEZVOUSHASHING

# @@protoc_insertion_point(module_scope)