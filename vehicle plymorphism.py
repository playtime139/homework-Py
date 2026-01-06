class BMW:
    def start(self):
        print("BMW is starting")

    def stop(self):
        print("BMW is stopping")


class Ferrari:
    def start(self):
        print("Ferrari is starting")

    def stop(self):
        print("Ferrari is stopping")


def operate_vehicle(vehicle):
    vehicle.start()
    vehicle.stop()


bmw = BMW()
ferrari = Ferrari()

operate_vehicle(bmw)
operate_vehicle(ferrari)
