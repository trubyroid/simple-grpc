import grpc
import sys

import ships_pb2 as shps
import ships_pb2_grpc as shps_g

from pydantic import BaseModel, validator


class Ship(BaseModel):
    crew_size: int
    length: float
    armed: bool
    alignment: int
    class_: int

    # @validator('crew_size')
    # def size_must_be(cls, v):
    #     if v < 4 or v > 500:
    #         print('must be more than 4 and less than 500')
    #     return v

    def check(self):
        if (self.class_ == 0):
            if (self.length < 80 or self.length > 250 or
                    self.crew_size < 4 or self.crew_size > 10):
                return None
        if (self.class_ == 1):
            if (self.length < 300 or self.length > 600 or
                self.crew_size < 10 or self.crew_size > 15 or
                    self.alignment == 1):
                return None
        if (self.class_ == 2):
            if (self.length < 500 or self.length > 1000 or
                    self.crew_size < 15 or self.crew_size > 30):
                return None
        if (self.class_ == 3):
            if (self.length < 800 or self.length > 2000 or
                self.crew_size < 50 or self.crew_size > 80 or
                    self.alignment == 1):
                return None
        if (self.class_ == 4):
            if (self.length < 1000 or self.length > 4000 or
                self.crew_size < 120 or self.crew_size > 250 or
                    self.armed is True):
                return None
        if (self.class_ == 5):
            if (self.length < 5000 or self.length > 20000 or
                    self.crew_size < 300 or self.crew_size > 500):
                return None
        return True


def parse_ship(ship):
    obj = Ship(crew_size=str(ship.crew_size),
               length=float(ship.length), armed=bool(ship.armed),
               alignment=int(ship.alignment), class_=int(ship.class_))
    return obj.check()


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
        j = 0
        for i in response.ships:
            j += 1
            print(j)
            shi = parse_ship(i)
            if shi is not None:
                print(i)


if __name__ == '__main__':
    run()
