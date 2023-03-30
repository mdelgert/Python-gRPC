#$ python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. my_service.proto

from concurrent import futures
import logging
import grpc
import my_service_pb2
import my_service_pb2_grpc

class MyServiceServicer(my_service_pb2_grpc.MyServiceServicer):
    def StreamMessages(self, request_iterator, context):
        for request in request_iterator:
            # Do some processing with request
            response = my_service_pb2.MyResponse(response="Received message: {}".format(request.message))
            yield response

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    my_service_pb2_grpc.add_MyServiceServicer_to_server(MyServiceServicer(), server)
    server.add_insecure_port('[::]:50052')
    server.start()
    server.wait_for_termination()
    print("Messages Server started!")

if __name__ == '__main__':
    logging.basicConfig()
    serve()