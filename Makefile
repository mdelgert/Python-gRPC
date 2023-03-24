wsl1:
	python3 -m grpc_tools.protoc -I ./protobufs --python_out=. --grpc_python_out=. ./protobufs/teams.proto && \
    python3 -m grpc_tools.protoc -I ./protobufs --python_out=. --grpc_python_out=. ./protobufs/hello.proto

dev2:
	#TODO