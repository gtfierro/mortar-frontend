# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import hod_pb2 as hod__pb2


class HodDBStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.ExecuteQuery = channel.unary_unary(
        '/proto.HodDB/ExecuteQuery',
        request_serializer=hod__pb2.QueryRequest.SerializeToString,
        response_deserializer=hod__pb2.QueryResponse.FromString,
        )


class HodDBServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def ExecuteQuery(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_HodDBServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'ExecuteQuery': grpc.unary_unary_rpc_method_handler(
          servicer.ExecuteQuery,
          request_deserializer=hod__pb2.QueryRequest.FromString,
          response_serializer=hod__pb2.QueryResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'proto.HodDB', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))