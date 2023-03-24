# Python-gRPC
https://www.linode.com/docs/guides/using-grpc-for-remote-procedural-calls/
https://grpc.io/docs/languages/python/quickstart/#generate-grpc-code
https://github.com/grpc-ecosystem/grpc-gateway#usage
https://www.linode.com/docs/guides/using-grpc-for-remote-procedural-calls/

# Protocol Buffers
https://www.educative.io/answers/what-is-protocol-buffers
https://protobuf.dev/programming-guides/proto3/

# Setup
virtualenv venv

# Installing Python Packages From a Requirements File
pip install -r requirements.txt

# How to Create a Python Requirements File
https://learnpython.com/blog/python-requirements-file/
pip freeze > requirements.txt

# Install gRPC.
sudo python3 -m pip install grpcio

# Install the gRPC tools. This also installs the protocol buffer compiler protoc.
sudo python3 -m pip install grpcio-tools