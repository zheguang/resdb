# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: RendezvousNode.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
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
  serialized_pb=b'\n\x14RendezvousNode.proto\"Z\n\x0eNodeGetRequest\x12\x1d\n\x04type\x18\x01 \x01(\x0e\x32\x0f.GetRequestType\x12\x0b\n\x03key\x18\x02 \x01(\t\x12\x12\n\x05value\x18\x03 \x01(\tH\x00\x88\x01\x01\x42\x08\n\x06_value\",\n\x0cNodeGetReply\x12\x12\n\x05value\x18\x01 \x01(\tH\x00\x88\x01\x01\x42\x08\n\x06_value\"&\n\x17NodeHashValueForRequest\x12\x0b\n\x03key\x18\x01 \x01(\t\"*\n\x15NodeHashValueForReply\x12\x11\n\thashValue\x18\x01 \x01(\x02\"2\n\x1cNodeSendItemToNewNodeRequest\x12\x12\n\nip_address\x18\x01 \x01(\t\"\x0b\n\tNodeEmpty*:\n\x0eGetRequestType\x12\x07\n\x03\x41\x44\x44\x10\x00\x12\n\n\x06UPDATE\x10\x01\x12\x07\n\x03GET\x10\x02\x12\n\n\x06\x44\x45LETE\x10\x03\x32\xd3\x01\n\x0eRendezvousNode\x12\x31\n\x0bget_request\x12\x0f.NodeGetRequest\x1a\r.NodeGetReply\"\x00\x30\x01\x12H\n\x12hash_value_for_key\x12\x18.NodeHashValueForRequest\x1a\x16.NodeHashValueForReply\"\x00\x12\x44\n\x15send_item_to_new_node\x12\x1d.NodeSendItemToNewNodeRequest\x1a\n.NodeEmpty\"\x00\x62\x06proto3'
)

_GETREQUESTTYPE = _descriptor.EnumDescriptor(
  name='GetRequestType',
  full_name='GetRequestType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ADD', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='UPDATE', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='GET', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DELETE', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=311,
  serialized_end=369,
)
_sym_db.RegisterEnumDescriptor(_GETREQUESTTYPE)

GetRequestType = enum_type_wrapper.EnumTypeWrapper(_GETREQUESTTYPE)
ADD = 0
UPDATE = 1
GET = 2
DELETE = 3



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
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
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
    _descriptor.OneofDescriptor(
      name='_value', full_name='NodeGetRequest._value',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=24,
  serialized_end=114,
)


_NODEGETREPLY = _descriptor.Descriptor(
  name='NodeGetReply',
  full_name='NodeGetReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='NodeGetReply.value', index=0,
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
    _descriptor.OneofDescriptor(
      name='_value', full_name='NodeGetReply._value',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=116,
  serialized_end=160,
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
  serialized_start=162,
  serialized_end=200,
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
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=202,
  serialized_end=244,
)


_NODESENDITEMTONEWNODEREQUEST = _descriptor.Descriptor(
  name='NodeSendItemToNewNodeRequest',
  full_name='NodeSendItemToNewNodeRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='ip_address', full_name='NodeSendItemToNewNodeRequest.ip_address', index=0,
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
  serialized_start=246,
  serialized_end=296,
)


_NODEEMPTY = _descriptor.Descriptor(
  name='NodeEmpty',
  full_name='NodeEmpty',
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
  serialized_start=298,
  serialized_end=309,
)

_NODEGETREQUEST.fields_by_name['type'].enum_type = _GETREQUESTTYPE
_NODEGETREQUEST.oneofs_by_name['_value'].fields.append(
  _NODEGETREQUEST.fields_by_name['value'])
_NODEGETREQUEST.fields_by_name['value'].containing_oneof = _NODEGETREQUEST.oneofs_by_name['_value']
_NODEGETREPLY.oneofs_by_name['_value'].fields.append(
  _NODEGETREPLY.fields_by_name['value'])
_NODEGETREPLY.fields_by_name['value'].containing_oneof = _NODEGETREPLY.oneofs_by_name['_value']
DESCRIPTOR.message_types_by_name['NodeGetRequest'] = _NODEGETREQUEST
DESCRIPTOR.message_types_by_name['NodeGetReply'] = _NODEGETREPLY
DESCRIPTOR.message_types_by_name['NodeHashValueForRequest'] = _NODEHASHVALUEFORREQUEST
DESCRIPTOR.message_types_by_name['NodeHashValueForReply'] = _NODEHASHVALUEFORREPLY
DESCRIPTOR.message_types_by_name['NodeSendItemToNewNodeRequest'] = _NODESENDITEMTONEWNODEREQUEST
DESCRIPTOR.message_types_by_name['NodeEmpty'] = _NODEEMPTY
DESCRIPTOR.enum_types_by_name['GetRequestType'] = _GETREQUESTTYPE
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

NodeSendItemToNewNodeRequest = _reflection.GeneratedProtocolMessageType('NodeSendItemToNewNodeRequest', (_message.Message,), {
  'DESCRIPTOR' : _NODESENDITEMTONEWNODEREQUEST,
  '__module__' : 'RendezvousNode_pb2'
  # @@protoc_insertion_point(class_scope:NodeSendItemToNewNodeRequest)
  })
_sym_db.RegisterMessage(NodeSendItemToNewNodeRequest)

NodeEmpty = _reflection.GeneratedProtocolMessageType('NodeEmpty', (_message.Message,), {
  'DESCRIPTOR' : _NODEEMPTY,
  '__module__' : 'RendezvousNode_pb2'
  # @@protoc_insertion_point(class_scope:NodeEmpty)
  })
_sym_db.RegisterMessage(NodeEmpty)



_RENDEZVOUSNODE = _descriptor.ServiceDescriptor(
  name='RendezvousNode',
  full_name='RendezvousNode',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=372,
  serialized_end=583,
  methods=[
  _descriptor.MethodDescriptor(
    name='get_request',
    full_name='RendezvousNode.get_request',
    index=0,
    containing_service=None,
    input_type=_NODEGETREQUEST,
    output_type=_NODEGETREPLY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='hash_value_for_key',
    full_name='RendezvousNode.hash_value_for_key',
    index=1,
    containing_service=None,
    input_type=_NODEHASHVALUEFORREQUEST,
    output_type=_NODEHASHVALUEFORREPLY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='send_item_to_new_node',
    full_name='RendezvousNode.send_item_to_new_node',
    index=2,
    containing_service=None,
    input_type=_NODESENDITEMTONEWNODEREQUEST,
    output_type=_NODEEMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_RENDEZVOUSNODE)

DESCRIPTOR.services_by_name['RendezvousNode'] = _RENDEZVOUSNODE

# @@protoc_insertion_point(module_scope)
