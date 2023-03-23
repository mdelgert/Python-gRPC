# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import hello_pb2 as hello__pb2


class HellosStub(object):
    """The hellos service definition.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetHello = channel.unary_unary(
                '/Hellos/GetHello',
                request_serializer=hello__pb2.HelloRequest.SerializeToString,
                response_deserializer=hello__pb2.HelloResponse.FromString,
                )


class HellosServicer(object):
    """The hellos service definition.
    """

    def GetHello(self, request, context):
        """Returns response.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_HellosServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetHello': grpc.unary_unary_rpc_method_handler(
                    servicer.GetHello,
                    request_deserializer=hello__pb2.HelloRequest.FromString,
                    response_serializer=hello__pb2.HelloResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Hellos', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Hellos(object):
    """The hellos service definition.
    """

    @staticmethod
    def GetHello(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Hellos/GetHello',
            hello__pb2.HelloRequest.SerializeToString,
            hello__pb2.HelloResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
