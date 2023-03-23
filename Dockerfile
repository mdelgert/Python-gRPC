FROM ubuntu:latest

RUN apt update && apt install python3 python3-pip sudo -y

RUN python3 -m pip install grpcio

RUN python3 -m pip install grpcio-tools

COPY teams teams

EXPOSE 50051

#https://stackoverflow.com/questions/29663459/python-app-does-not-print-anything-when-running-detached-in-docker
CMD ["python3", "-u", "./teams/teams_server.py"]