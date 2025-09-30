class Car():
    def __init__(self,brand,model):
        self.__brand = brand # (__) makes it private 
        self.__model = model

    def get_brand(self):  # so thats why we need to define getter method
        return self.__brand

my_car = Car("Toyota","Corolla") 

print(my_car.get_brand())
print(my_car.__brand)













# class ElectricCar(Car):
#     def __init__(self,brand,model,battery_size):
#         super().__init__(brand,model)
#         self.battery_size = battery_size
#     def ev_info(self):
#         return f"{self.brand} {self.model} {self.battery_size}"

