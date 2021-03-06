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


import src.grpc_enums.type_pb2 as type__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='RendezvousNode.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x14RendezvousNode.proto\x1a\ntype.proto\"d\n\x0eNodeGetRequest\x12\x1d\n\x04type\x18\x01 \x01(\x0e\x32\x0f.GetRequestType\x12\x0b\n\x03key\x18\x02 \x01(\t\x12\x0e\n\x06values\x18\x03 \x03(\t\x12\x16\n\x0ereplica_number\x18\x04 \x01(\x05\"\x1e\n\x0cNodeGetReply\x12\x0e\n\x06values\x18\x01 \x03(\t\"/\n\x19NodeGetLostEntriesRequest\x12\x12\n\nip_address\x18\x01 \x01(\t\"?\n\x13NodeGetObjectsReply\x12\x10\n\x03key\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x0e\n\x06values\x18\x02 \x03(\tB\x06\n\x04_key\"@\n\x14NodeGetReplicasReply\x12\x10\n\x03key\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x0e\n\x06values\x18\x02 \x03(\tB\x06\n\x04_key\"&\n\x17NodeHashValueForRequest\x12\x0b\n\x03key\x18\x01 \x01(\t\"*\n\x15NodeHashValueForReply\x12\x11\n\thashValue\x18\x01 \x01(\x02\"2\n\x1cNodeSendItemToNewNodeRequest\x12\x12\n\nip_address\x18\x01 \x01(\t\"\x0b\n\tNodeEmpty2\xa5\x03\n\x0eRendezvousNode\x12/\n\x0bget_request\x12\x0f.NodeGetRequest\x1a\r.NodeGetReply\"\x00\x12\x33\n\x0bget_objects\x12\n.NodeEmpty\x1a\x14.NodeGetObjectsReply\"\x00\x30\x01\x12\x35\n\x0cget_replicas\x12\n.NodeEmpty\x1a\x15.NodeGetReplicasReply\"\x00\x30\x01\x12@\n\x14inspect_lost_entries\x12\x1a.NodeGetLostEntriesRequest\x1a\n.NodeEmpty\"\x00\x12H\n\x12hash_value_for_key\x12\x18.NodeHashValueForRequest\x1a\x16.NodeHashValueForReply\"\x00\x12\x44\n\x15send_item_to_new_node\x12\x1d.NodeSendItemToNewNodeRequest\x1a\n.NodeEmpty\"\x00\x12$\n\nremove_all\x12\n.NodeEmpty\x1a\n.NodeEmptyb\x06proto3'
  ,
  dependencies=[type__pb2.DESCRIPTOR,])




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
      name='values', full_name='NodeGetRequest.values', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='replica_number', full_name='NodeGetRequest.replica_number', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=36,
  serialized_end=136,
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
      name='values', full_name='NodeGetReply.values', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=138,
  serialized_end=168,
)


_NODEGETLOSTENTRIESREQUEST = _descriptor.Descriptor(
  name='NodeGetLostEntriesRequest',
  full_name='NodeGetLostEntriesRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='ip_address', full_name='NodeGetLostEntriesRequest.ip_address', index=0,
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
  serialized_start=170,
  serialized_end=217,
)


_NODEGETOBJECTSREPLY = _descriptor.Descriptor(
  name='NodeGetObjectsReply',
  full_name='NodeGetObjectsReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='NodeGetObjectsReply.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='values', full_name='NodeGetObjectsReply.values', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
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
      name='_key', full_name='NodeGetObjectsReply._key',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=219,
  serialized_end=282,
)


_NODEGETREPLICASREPLY = _descriptor.Descriptor(
  name='NodeGetReplicasReply',
  full_name='NodeGetReplicasReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='NodeGetReplicasReply.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='values', full_name='NodeGetReplicasReply.values', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
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
      name='_key', full_name='NodeGetReplicasReply._key',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=284,
  serialized_end=348,
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
  serialized_start=350,
  serialized_end=388,
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
  serialized_start=390,
  serialized_end=432,
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
  serialized_start=434,
  serialized_end=484,
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
  serialized_start=486,
  serialized_end=497,
)

_NODEGETREQUEST.fields_by_name['type'].enum_type = type__pb2._GETREQUESTTYPE
_NODEGETOBJECTSREPLY.oneofs_by_name['_key'].fields.append(
  _NODEGETOBJECTSREPLY.fields_by_name['key'])
_NODEGETOBJECTSREPLY.fields_by_name['key'].containing_oneof = _NODEGETOBJECTSREPLY.oneofs_by_name['_key']
_NODEGETREPLICASREPLY.oneofs_by_name['_key'].fields.append(
  _NODEGETREPLICASREPLY.fields_by_name['key'])
_NODEGETREPLICASREPLY.fields_by_name['key'].containing_oneof = _NODEGETREPLICASREPLY.oneofs_by_name['_key']
DESCRIPTOR.message_types_by_name['NodeGetRequest'] = _NODEGETREQUEST
DESCRIPTOR.message_types_by_name['NodeGetReply'] = _NODEGETREPLY
DESCRIPTOR.message_types_by_name['NodeGetLostEntriesRequest'] = _NODEGETLOSTENTRIESREQUEST
DESCRIPTOR.message_types_by_name['NodeGetObjectsReply'] = _NODEGETOBJECTSREPLY
DESCRIPTOR.message_types_by_name['NodeGetReplicasReply'] = _NODEGETREPLICASREPLY
DESCRIPTOR.message_types_by_name['NodeHashValueForRequest'] = _NODEHASHVALUEFORREQUEST
DESCRIPTOR.message_types_by_name['NodeHashValueForReply'] = _NODEHASHVALUEFORREPLY
DESCRIPTOR.message_types_by_name['NodeSendItemToNewNodeRequest'] = _NODESENDITEMTONEWNODEREQUEST
DESCRIPTOR.message_types_by_name['NodeEmpty'] = _NODEEMPTY
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

NodeGetLostEntriesRequest = _reflection.GeneratedProtocolMessageType('NodeGetLostEntriesRequest', (_message.Message,), {
  'DESCRIPTOR' : _NODEGETLOSTENTRIESREQUEST,
  '__module__' : 'RendezvousNode_pb2'
  # @@protoc_insertion_point(class_scope:NodeGetLostEntriesRequest)
  })
_sym_db.RegisterMessage(NodeGetLostEntriesRequest)

NodeGetObjectsReply = _reflection.GeneratedProtocolMessageType('NodeGetObjectsReply', (_message.Message,), {
  'DESCRIPTOR' : _NODEGETOBJECTSREPLY,
  '__module__' : 'RendezvousNode_pb2'
  # @@protoc_insertion_point(class_scope:NodeGetObjectsReply)
  })
_sym_db.RegisterMessage(NodeGetObjectsReply)

NodeGetReplicasReply = _reflection.GeneratedProtocolMessageType('NodeGetReplicasReply', (_message.Message,), {
  'DESCRIPTOR' : _NODEGETREPLICASREPLY,
  '__module__' : 'RendezvousNode_pb2'
  # @@protoc_insertion_point(class_scope:NodeGetReplicasReply)
  })
_sym_db.RegisterMessage(NodeGetReplicasReply)

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
  serialized_start=500,
  serialized_end=921,
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
    name='get_objects',
    full_name='RendezvousNode.get_objects',
    index=1,
    containing_service=None,
    input_type=_NODEEMPTY,
    output_type=_NODEGETOBJECTSREPLY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='get_replicas',
    full_name='RendezvousNode.get_replicas',
    index=2,
    containing_service=None,
    input_type=_NODEEMPTY,
    output_type=_NODEGETREPLICASREPLY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='inspect_lost_entries',
    full_name='RendezvousNode.inspect_lost_entries',
    index=3,
    containing_service=None,
    input_type=_NODEGETLOSTENTRIESREQUEST,
    output_type=_NODEEMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='hash_value_for_key',
    full_name='RendezvousNode.hash_value_for_key',
    index=4,
    containing_service=None,
    input_type=_NODEHASHVALUEFORREQUEST,
    output_type=_NODEHASHVALUEFORREPLY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='send_item_to_new_node',
    full_name='RendezvousNode.send_item_to_new_node',
    index=5,
    containing_service=None,
    input_type=_NODESENDITEMTONEWNODEREQUEST,
    output_type=_NODEEMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='remove_all',
    full_name='RendezvousNode.remove_all',
    index=6,
    containing_service=None,
    input_type=_NODEEMPTY,
    output_type=_NODEEMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_RENDEZVOUSNODE)

DESCRIPTOR.services_by_name['RendezvousNode'] = _RENDEZVOUSNODE

# @@protoc_insertion_point(module_scope)
