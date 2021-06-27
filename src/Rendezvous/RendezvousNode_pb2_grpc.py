# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import src.Rendezvous.RendezvousNode_pb2 as RendezvousNode__pb2


class RendezvousNodeStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.hash_value_for_key = channel.unary_unary(
                '/RendezvousNode/hash_value_for_key',
                request_serializer=RendezvousNode__pb2.NodeHashValueForRequest.SerializeToString,
                response_deserializer=RendezvousNode__pb2.NodeHashValueForReply.FromString,
                )
        self.get_request = channel.unary_unary(
                '/RendezvousNode/get_request',
                request_serializer=RendezvousNode__pb2.NodeGetRequest.SerializeToString,
                response_deserializer=RendezvousNode__pb2.NodeGetReply.FromString,
                )


class RendezvousNodeServicer(object):
    """Missing associated documentation comment in .proto file."""

    def hash_value_for_key(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def get_request(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_RendezvousNodeServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'hash_value_for_key': grpc.unary_unary_rpc_method_handler(
                    servicer.hash_value_for_key,
                    request_deserializer=RendezvousNode__pb2.NodeHashValueForRequest.FromString,
                    response_serializer=RendezvousNode__pb2.NodeHashValueForReply.SerializeToString,
            ),
            'get_request': grpc.unary_unary_rpc_method_handler(
                    servicer.get_request,
                    request_deserializer=RendezvousNode__pb2.NodeGetRequest.FromString,
                    response_serializer=RendezvousNode__pb2.NodeGetReply.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'RendezvousNode', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class RendezvousNode(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def hash_value_for_key(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/RendezvousNode/hash_value_for_key',
            RendezvousNode__pb2.NodeHashValueForRequest.SerializeToString,
            RendezvousNode__pb2.NodeHashValueForReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def get_request(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/RendezvousNode/get_request',
            RendezvousNode__pb2.NodeGetRequest.SerializeToString,
            RendezvousNode__pb2.NodeGetReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
