from concurrent import futures

import grpc

from code import FresnoDailyNews_pb2_grpc, FresnoDailyNews_pb2
from code.pythonrpcmethods import extract_keywords


class FresnoDailyNews(FresnoDailyNews_pb2_grpc.FresnoDailyNewsServicer):
    def ExtractKeyword(self, request, context):
        print("Got request " + str(request))
        return FresnoDailyNews_pb2.ExtractKeywordsResponse(reply=extract_keywords(request.message))


def server():
    grpc_server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
    FresnoDailyNews_pb2_grpc.add_FresnoDailyNewsServicer_to_server(FresnoDailyNews(), grpc_server)
    grpc_server.add_insecure_port('[::]:50051')
    print("Listening on port 50051...")
    grpc_server.start()
    grpc_server.wait_for_termination()
