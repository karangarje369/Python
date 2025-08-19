str = "Chai Masala"
firstChar = str[0]
print(str[0])
print(firstChar)

#Slicing
slice_chai = str[5:11] # this is how we slice the string (:)
print(slice_chai)

num_list = "0123456789"
print(num_list[:]) # prints as it is
print(num_list[5:]) # from 5 till end
print(num_list[:11]) # from 11 till stsrt
print(num_list[0:7:2]) # 
print(num_list[0:7:3]) # 

# Methods in String 

# lowercase uppercase 
str1 = "Chai"
print(str1.lower())
print(str1.upper())

# spaces manage 
str2 = "   masala chai "
print(str2.strip())

# replace 
str3 = "Lemon Chai"
print(str3.replace("Lemon","Ginger"))

# seperating . Converting to list (on the basis of ",")
str4 = "lemon,ginger,masala,mint"
print(str4.split(","))

# Find 
str5 = "lemon chai"
print(str5.find("chai"))

# Count 
str6 = "masala chai chai chai chai "
print(str6.count("chai"))

# adding variables to string
str7 = "i am {}"
name = "Karan"
print(str7.format(name)) # here we can pass multiple values

# List to String
list1 = ['lemon', 'ginger', 'masala', 'mint']
print(" ".join(list1))