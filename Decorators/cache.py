import time 

def cache(func):
    chache_value = {}
    print(chache_value)
    def wrapper(*args):
        if args in chache_value:
            return chache_value[args]
        
        result = func(*args)
        chache_value[args] = result

        return result
    
    return wrapper

@cache
def fun(a,b):
    time.sleep(4)
    return a + b

print(fun(2,2))
# fun(2,2)