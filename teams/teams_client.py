from __future__ import print_function
import logging

import grpc

import teams_pb2
import teams_pb2_grpc

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = teams_pb2_grpc.TeamsStub(channel)
        response = stub.GetTeam(teams_pb2.TeamRequest(city='Chicago'))
        print("Teams client received: " + response.city + " " + response.nickname)
        response = stub.GetTeam(teams_pb2.TeamRequest(city='Philadelphia'))
        print("Teams client received: " + response.city + " " + response.nickname)
        response = stub.GetTeam(teams_pb2.TeamRequest(city='Miami'))
        print("Teams client received: " + response.city + " " + response.nickname)

if __name__ == '__main__':
    logging.basicConfig()
    run()