from concurrent import futures
import logging

import grpc

import teams_pb2
import teams_pb2_grpc
class Teams(teams_pb2_grpc.TeamsServicer):

    def GetTeam(self, request, context):
        metadata = dict(context.invocation_metadata())
        print(metadata)
        print("Received:" + request.city)
        teamList = { 'Chicago' : 'Jackals',
                     'Detroit' : 'Wheels',
                     'Minneapolis' : 'Nordics',
                     'New York' : 'Metros',
                     'Arizona' : 'Roadrunners',
                     'San Francisco' : 'Stingers',
                     'Seattle' : 'Orcas',
                     'Los Angeles' : 'Pumas',
                     'Philadelphia' : 'Foxes',
                     'Boston' : 'Revolutionaries' }
        if request.city in teamList:
            team_name = teamList[request.city]
        else:
            team_name = 'not a member'
        return teams_pb2.TeamResponse(city=request.city, nickname=team_name)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    teams_pb2_grpc.add_TeamsServicer_to_server(Teams(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()
    print("Server started!")

if __name__ == '__main__':
    logging.basicConfig()
    serve()
    