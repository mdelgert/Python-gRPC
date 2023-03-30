import grpc
import my_service_pb2
import my_service_pb2_grpc

channel = grpc.insecure_channel('localhost:50052')
stub = my_service_pb2_grpc.MyServiceStub(channel)

requests = [my_service_pb2.MyRequest(message="Hello"), my_service_pb2.MyRequest(message="World")]
responses = stub.StreamMessages(iter(requests))

for response in responses:
    print(response.response)
