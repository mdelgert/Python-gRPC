dev1:
	python -m grpc_tools.protoc -I ./protobufs --python_out=. --grpc_python_out=. ./protobufs/teams.proto && \
    python -m grpc_tools.protoc -I ./protobufs --python_out=. --grpc_python_out=. ./protobufs/hello.proto && \
    python -m grpc_tools.protoc -I ./protobufs --python_out=./protobufs --grpc_python_out=./protobufs ./protobufs/messages.proto
    python -m grpc_tools.protoc -I ./protobufs --python_out=. --grpc_python_out=. ./protobufs/messages.proto
dev2:
	#TODO