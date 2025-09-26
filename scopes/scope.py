x = 10 
def func():
    #  x= 10
    print(x)

def func2():
    global x 
    x = 9

func2()
print(x)

def func3(y):
    def actual(x):
        return x ** y
    return actual 

f = func3(2)
f2 = func3(3)

print(f(3))
print(f2(3))