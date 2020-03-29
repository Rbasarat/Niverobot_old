# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import dateparser_pb2 as dateparser__pb2


class DateParserStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.ParseDate = channel.unary_unary(
        '/dateparser.DateParser/ParseDate',
        request_serializer=dateparser__pb2.ParseDateRequest.SerializeToString,
        response_deserializer=dateparser__pb2.ParseDateReply.FromString,
        )


class DateParserServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def ParseDate(self, request, context):
    """Parses natural date to datetime object
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_DateParserServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'ParseDate': grpc.unary_unary_rpc_method_handler(
          servicer.ParseDate,
          request_deserializer=dateparser__pb2.ParseDateRequest.FromString,
          response_serializer=dateparser__pb2.ParseDateReply.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'dateparser.DateParser', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
