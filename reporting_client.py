import grpc
import sys

import ships_pb2 as shps
import ships_pb2_grpc as shps_g


def run():
    print("\n\nSearch ...\n\n")
    if len(sys.argv) != 2:
        print("Insert string with coordinates.")
        exit()
    if sys.argv[1] != "17 45 40.0409 -29 00 28.118":
        print("Invalid coordinates.")
        exit()
    request = shps.Request()
    request.coordinates = sys.argv[1]

    with grpc.insecure_channel('localhost:50051') as channel:
        stub = shps_g.GreeterStub(channel)
        response = stub.Transmitter(request)
        print("Ships in this galaxy:")
        for i in response.ships:
            print(str(i) + "\n")


if __name__ == '__main__':
    run()
