def sum_all(*args):
    print(args) #This returns a tuple
    print(*args) # This returns current value 
    # return sum(args)

    # for i in args:
    #     print(i)

print(sum_all(1,2,3,4,6))