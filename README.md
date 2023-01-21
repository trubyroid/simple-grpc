# simple-grpc

For test task:
1.Proto files
python3 -m grpc_tools.protoc -I protos --python_out=. --grpc_python_out=. protos/ships.proto

2. Server
python3 .\reporting_server.py

3. Client (other terminal)
python3 .\reporting_client.py "17 45 40.0409 -29 00 28.118"