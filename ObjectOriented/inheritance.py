class Car():
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

    def fullname(self):
        return f"{self.brand} {self.model}"

class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size
    def ev_info(self):
        return f"{self.brand} {self.model} {self.battery_size}"

# mycar = Car("Toyota","Etios")
# # print(mycar.brand ," ", mycar.model)
# print(mycar.fullname())

ev = ElectricCar("Tata","Nexon","500")     
# print(ev.fullname())
print(ev.ev_info())