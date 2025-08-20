chaiList = ['Lemon','Green','Ginger','Masala']
print(chaiList)
print(chaiList[-1])
print(chaiList[1:3])
print(chaiList[:3])
print(chaiList[3:])

chaiList[1:2] = ["White"] # replacing an element in list 
print(chaiList)

chaiList[1:3] = ["Ginger","jaggery"]
print(chaiList)

chaiList[1:1] = ["test","test"]
print(chaiList)

chaiList[1:3] = [] # delete or nothing operation

# Append method 
chaiList.append("oolong")

for tea in chaiList:
    print(tea)

if "oolong" in chaiList:
    print("True")   

# pop method 
chaiList.pop()        
print(chaiList)

# remove method 
chaiList.remove("Lemon")
print(chaiList)

# insert Method 
chaiList.insert(1,"Lemon")
print(chaiList)

# copy method 
tea_copy = chaiList.copy() # here both holds diffrent refrence
print(tea_copy)

# range 
r = range(10)
print(r)

#String Comprehension
squared_num = [x**2 for x in range(10)]
print(squared_num)

