dev1:
	cd teams
	python -m grpc_tools.protoc -I ./protobufs --python_out=. --grpc_python_out=. ./protobufs/teams.proto

dev2:
	#TODO