echo "Start compiling"

protoc -I=./ --go_out=plugins=grpc:../api/grpcGeneratedCode ./*.proto
python3 -m grpc_tools.protoc -I=./ --python_out=../behavior-analysis-core/grpcGeneratedCode/ --grpc_python_out=../behavior-analysis-core/grpcGeneratedCode/ ./*.proto

echo "Done"
