from concurrent import futures
import logging
import grpc
import messages_pb2
import messages_pb2_grpc
import serverDb

class Messages(messages_pb2_grpc.MessagesServicer):

    def GetMessage(self, request, context):
        metadata = dict(context.invocation_metadata())
        #print(metadata)
        #print("Received:" + request.message)
        serverDb.createMessage(request.message)
        return messages_pb2.MessageResponse(message=request.message, messageType='get')

    def CreateMessage(self, request, context):
        serverDb.createMessage(request.message)
        return messages_pb2.MessageResponse(message=request.message, messageType='create')
    
    def DeleteMessages(self, request, context):
        serverDb.deleteMessages()
        return messages_pb2.MessageResponse(message=request.message, messageType='delete')
    
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    messages_pb2_grpc.add_MessagesServicer_to_server(Messages(), server)
    server.add_insecure_port('[::]:50052')
    server.start()
    server.wait_for_termination()
    print("Messages Server started!")

if __name__ == '__main__':
    logging.basicConfig()
    serve()
    