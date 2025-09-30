class Car():
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

    def fullname(self):
        return f"{self.brand} {self.model}"

mycar = Car("Toyota","Etios")
# print(mycar.brand ," ", mycar.model)
print(mycar.fullname())