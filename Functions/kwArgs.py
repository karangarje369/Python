# named parameters
# def kwargs(name, power):
#     print("Name ",name , "Power ", power)

# kwargs(name="karan" , power="learning") # this are named parameters
# # anyway if we change the position still it dont affect the function will sort it according to the name 
# kwargs(power="learning" , name="karan")

def kwargs(**kwargs):
    for key,value in kwargs.items():
        print(f"Key={key}, value={value}")

kwargs(name="karan",age="21")        
kwargs(name="harsh",age="21")        

