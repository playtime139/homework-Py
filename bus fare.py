class Vehicle:
    def __init__(self, base_fare):
        self.base_fare = base_fare

class Bus(Vehicle):
    def __init__(self, base_fare, distance):
        super().__init__(base_fare)
        self.distance = distance

    def calculate_fare(self):
        fare_per_km = 2  
        total_fare = self.base_fare + (self.distance * fare_per_km)
        return total_fare


bus = Bus(5, 10) 
print("Total Bus Fare:", bus.calculate_fare())
