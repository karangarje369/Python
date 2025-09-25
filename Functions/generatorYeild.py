def yieldFun(limit):
    for i in range(0,limit+1,2):
        yield i

for i in yieldFun(10):
    print(i)      

# instead of return we use yield . yield remembers or has track of function 
    
    
