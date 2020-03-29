from __future__ import print_function
import logging

import grpc

import dateparser_pb2
import dateparser_pb2_grpc


def run():
    with grpc.insecure_channel('localhost:3001') as channel:
        stub = dateparser_pb2_grpc.DateParserStub(channel)
        response = stub.ParseDate(
            dateparser_pb2.ParseDateRequest(NaturalDate='you'))
    print("Greeter client received: " + response.ParsedDate)


if __name__ == '__main__':
    logging.basicConfig()
    run()
