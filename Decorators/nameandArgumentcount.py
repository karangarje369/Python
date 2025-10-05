def deco(func):
    def wrapper(*args,**kwargs):
       result = func(*args,**kwargs)
       args_value = ", ".join(str(arg) for arg in args)
       kwargs_value = ", ".join(f"{k}={v}" for k,v in kwargs.items())
       print(f"args={args_value} kwargs = {kwargs_value}")
       print(f"function:{func.__name__}")
       
    return wrapper   

@deco
def hello():
    print("abav")

hello()

@deco
def greet(name, greeting="hello"):
    pass

greet("Karan", greeting="Hello")    