# static method that is only accessible by class not instance
class Car():
    def __init__(self,brand,model):
        self.brand = brand
        self.__model = model

    def fullname(self):
        return f"{self.brand} {self.__model}"
    
    @staticmethod
    def general_info():
        return "Cars info"
    
    @property
    def modle(self):
        return self.__model

my_car = Car("toyota","colloraa")

# making model read only property decorators 

print(my_car.modle)
my_car. __model = "city"
