from concurrent import futures
import random
import grpc

import ships_pb2 as shps
import ships_pb2_grpc as shps_g


class Server(shps_g.GreeterServicer):

    def __init__(self) -> None:
        self.resp = shps.Response()
        pass

    def Transmitter(self, request, context):
        print("Coordinates: ", str(request.coordinates))
        return self.set_of_ship_generator()

    def set_of_ship_generator(self) -> list:
        classes = [shps.Response.Corvette, shps.Response.Frigate,
                   shps.Response.Cruiser, shps.Response.Destroyer,
                   shps.Response.Carrier, shps.Response.Dreadnought]
        allign = [shps.Response.Ally, shps.Response.Enemy]
        names_s = ["Executor", "Unknown", "Normandy",
                   "Gagak", "Tikari", "Bajovnik", "Lusitania Fleet",
                   "Oak", "Tiger", "Drag"]
        f_names_o = ['Gwen', 'John Paul', 'Teresa', 'Andrew',
                     'Peter', 'Shimon', 'Dink', 'Mosca',
                     'Mazer', 'Bob']
        l_names_o = ['Andersen', 'Arkanyan', 'Wiggin',
                     'Graff', 'Karbi', 'Madrid', 'Meeker',
                     'Molo', 'Chamrajnagar', 'Pace']
        ranks = ['Commander', 'Captain', 'General',
                 'Marshal', 'Generalissimus']
        galaxy = self.resp.Galaxy()

        for i in range(random.randint(1, 11)):
            new_ship = galaxy.ships.add()

            new_ship.crew_size = random.randint(4, 510)
            new_ship.length = random.uniform(80, 20000)
            new_ship.armed = random.choice([True, False])
            new_ship.class_ = random.choice(classes)

            new_ship.name = random.choice(names_s)
            if new_ship.name == "Unknown":
                new_ship.alignment = shps.Response.Enemy
            else:
                new_ship.alignment = random.choice(allign)
                qua_o = random.randint(1, 11)
                for i in range(qua_o):
                    officer = new_ship.officers.add()
                    officer.first_name = random.choice(f_names_o)
                    officer.last_name = random.choice(l_names_o)
                    officer.rank = random.choice(ranks)
        return galaxy

    def run_server(self):
        port = '50051'
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        shps_g.add_GreeterServicer_to_server(Server(), server)
        server.add_insecure_port('localhost:' + port)
        server.start()
        print("Server started, listening on " + port)
        server.wait_for_termination()


if __name__ == '__main__':
    srv = Server()
    srv.run_server()
