class Car():
    total_car = 0
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
        Car.total_car += 1

    def fullname(self):
        return f"{self.brand} {self.model}"
    
    def fuel_type(self):
        return "Diesel or petrol"
    

class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size
    def ev_info(self):
        return f"{self.brand} {self.model} {self.battery_size}"
    def fuel_type(self):
        return "Electricity"

mycar = Car("Toyota","Etios")
print(mycar.fuel_type())

ev = ElectricCar("Tata","Nexon","80kwh")     
print(ev.fuel_type())

# so here different classes has same name methods
# directly accessing class variable
print(Car.total_car)

