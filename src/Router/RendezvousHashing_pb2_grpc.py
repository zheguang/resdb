# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import src.Router.RendezvousHashing_pb2 as RendezvousHashing__pb2


class RendezvousHashingStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.forward_to_responsible_node = channel.unary_unary(
                '/RendezvousHashing/forward_to_responsible_node',
                request_serializer=RendezvousHashing__pb2.RendezvousFindNodeRequest.SerializeToString,
                response_deserializer=RendezvousHashing__pb2.RendezvousFindNodeResponse.FromString,
                )
        self.add_node = channel.unary_unary(
                '/RendezvousHashing/add_node',
                request_serializer=RendezvousHashing__pb2.RendezvousInformation.SerializeToString,
                response_deserializer=RendezvousHashing__pb2.RendezvousEmpty.FromString,
                )
        self.remove_node = channel.unary_unary(
                '/RendezvousHashing/remove_node',
                request_serializer=RendezvousHashing__pb2.RendezvousInformation.SerializeToString,
                response_deserializer=RendezvousHashing__pb2.RendezvousEmpty.FromString,
                )
        self._add_node = channel.unary_unary(
                '/RendezvousHashing/_add_node',
                request_serializer=RendezvousHashing__pb2.RendezvousInformation.SerializeToString,
                response_deserializer=RendezvousHashing__pb2.RendezvousEmpty.FromString,
                )
        self._remove_node = channel.unary_unary(
                '/RendezvousHashing/_remove_node',
                request_serializer=RendezvousHashing__pb2.RendezvousInformation.SerializeToString,
                response_deserializer=RendezvousHashing__pb2.RendezvousEmpty.FromString,
                )


class RendezvousHashingServicer(object):
    """Missing associated documentation comment in .proto file."""

    def forward_to_responsible_node(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def add_node(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def remove_node(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def _add_node(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def _remove_node(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_RendezvousHashingServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'forward_to_responsible_node': grpc.unary_unary_rpc_method_handler(
                    servicer.forward_to_responsible_node,
                    request_deserializer=RendezvousHashing__pb2.RendezvousFindNodeRequest.FromString,
                    response_serializer=RendezvousHashing__pb2.RendezvousFindNodeResponse.SerializeToString,
            ),
            'add_node': grpc.unary_unary_rpc_method_handler(
                    servicer.add_node,
                    request_deserializer=RendezvousHashing__pb2.RendezvousInformation.FromString,
                    response_serializer=RendezvousHashing__pb2.RendezvousEmpty.SerializeToString,
            ),
            'remove_node': grpc.unary_unary_rpc_method_handler(
                    servicer.remove_node,
                    request_deserializer=RendezvousHashing__pb2.RendezvousInformation.FromString,
                    response_serializer=RendezvousHashing__pb2.RendezvousEmpty.SerializeToString,
            ),
            '_add_node': grpc.unary_unary_rpc_method_handler(
                    servicer._add_node,
                    request_deserializer=RendezvousHashing__pb2.RendezvousInformation.FromString,
                    response_serializer=RendezvousHashing__pb2.RendezvousEmpty.SerializeToString,
            ),
            '_remove_node': grpc.unary_unary_rpc_method_handler(
                    servicer._remove_node,
                    request_deserializer=RendezvousHashing__pb2.RendezvousInformation.FromString,
                    response_serializer=RendezvousHashing__pb2.RendezvousEmpty.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'RendezvousHashing', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class RendezvousHashing(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def forward_to_responsible_node(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/RendezvousHashing/forward_to_responsible_node',
            RendezvousHashing__pb2.RendezvousFindNodeRequest.SerializeToString,
            RendezvousHashing__pb2.RendezvousFindNodeResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def add_node(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/RendezvousHashing/add_node',
            RendezvousHashing__pb2.RendezvousInformation.SerializeToString,
            RendezvousHashing__pb2.RendezvousEmpty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def remove_node(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/RendezvousHashing/remove_node',
            RendezvousHashing__pb2.RendezvousInformation.SerializeToString,
            RendezvousHashing__pb2.RendezvousEmpty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def _add_node(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/RendezvousHashing/_add_node',
            RendezvousHashing__pb2.RendezvousInformation.SerializeToString,
            RendezvousHashing__pb2.RendezvousEmpty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def _remove_node(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/RendezvousHashing/_remove_node',
            RendezvousHashing__pb2.RendezvousInformation.SerializeToString,
            RendezvousHashing__pb2.RendezvousEmpty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
