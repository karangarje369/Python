# input_num = 3
# count = 0
# i = 0
# while(i < input_num):
#     i += 1
#     if input_num%i == 0:  
#         count += 1


# if count==2:
#     print("isPrime") 
# else:
#     print("notPrime")      

number = 29 
is_prime = True 

if number > 1:
    for i in range(2,number):
        if(number%1 == 0):
            is_prime = False
            break

print(is_prime)        