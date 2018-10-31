# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from pymortar import mortar_pb2 as mortar__pb2


class MortarStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Qualify = channel.unary_unary(
        '/proto.Mortar/Qualify',
        request_serializer=mortar__pb2.QualifyRequest.SerializeToString,
        response_deserializer=mortar__pb2.QualifyResponse.FromString,
        )
    self.Fetch = channel.unary_unary(
        '/proto.Mortar/Fetch',
        request_serializer=mortar__pb2.FetchRequest.SerializeToString,
        response_deserializer=mortar__pb2.FetchResponse.FromString,
        )


class MortarServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def Qualify(self, request, context):
    """returns list of sites that match the qualification filter
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Fetch(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_MortarServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Qualify': grpc.unary_unary_rpc_method_handler(
          servicer.Qualify,
          request_deserializer=mortar__pb2.QualifyRequest.FromString,
          response_serializer=mortar__pb2.QualifyResponse.SerializeToString,
      ),
      'Fetch': grpc.unary_unary_rpc_method_handler(
          servicer.Fetch,
          request_deserializer=mortar__pb2.FetchRequest.FromString,
          response_serializer=mortar__pb2.FetchResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'proto.Mortar', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))