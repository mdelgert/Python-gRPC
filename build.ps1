docker build -t grpc:1.0 .

docker stop grpcTest

docker rm grpcTest

docker run -d -p 50051:50051 --name grpcTest grpc:1.0